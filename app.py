import random

import streamlit as st

# FIX: ChatGPT helped refactor the game rules out of the Streamlit UI so they can be tested directly.
from logic_utils import (
    check_guess,
    get_hint_message,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")


def reset_game() -> None:
    """Reset every piece of state that belongs to one game."""
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.game_difficulty = difficulty


if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "status" not in st.session_state:
    st.session_state.status = "playing"
if "history" not in st.session_state:
    st.session_state.history = []
if "game_difficulty" not in st.session_state:
    st.session_state.game_difficulty = difficulty
if "feedback" not in st.session_state:
    st.session_state.feedback = []

# FIX: AI review found that changing difficulty could leave a secret from the old range.
if st.session_state.game_difficulty != difficulty:
    reset_game()
    st.session_state.feedback = [
        ("success", f"Difficulty changed to {difficulty}. New game started.")
    ]

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {max(0, attempt_limit - st.session_state.attempts)}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}",
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

feedback = st.session_state.feedback
st.session_state.feedback = []
for kind, text in feedback:
    if kind == "success":
        st.success(text)
    elif kind == "warning":
        st.warning(text)
    elif kind == "error":
        st.error(text)

if new_game:
    # FIX: AI identified that the old code reset attempts and secret but left status, score, and history stale.
    reset_game()
    st.session_state.feedback = [("success", "New game started.")]
    st.rerun()

if st.session_state.status != "playing":
    if not feedback:
        if st.session_state.status == "won":
            st.success("You already won. Start a new game to play again.")
        else:
            st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    next_feedback = []
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        # Invalid text does not consume an attempt.
        next_feedback.append(("error", err))
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        # FIX: Keep both values numeric; the original code changed the secret to a string on alternating turns.
        outcome = check_guess(guess_int, st.session_state.secret)
        message = get_hint_message(outcome)

        if show_hint:
            next_feedback.append(("warning", message))

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.status = "won"
            next_feedback.append(
                (
                    "success",
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}",
                )
            )
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            next_feedback.append(
                (
                    "error",
                    f"Out of attempts! The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}",
                )
            )

    # A rerun makes the attempts-left banner and debug panel reflect the state change immediately.
    st.session_state.feedback = next_feedback
    st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
