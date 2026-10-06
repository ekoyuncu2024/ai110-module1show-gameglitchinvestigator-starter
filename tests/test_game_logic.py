from logic_utils import (
    check_guess,
    get_hint_message,
    parse_guess,
    update_score,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_large_negative_guess_tells_player_to_go_higher():
    # Reproduces the Phase 1 hint bug seen with secret 82.
    outcome = check_guess(-10**24, 82)
    assert outcome == "Too Low"
    assert get_hint_message(outcome) == "📉 Go HIGHER!"


def test_incorrect_guess_always_costs_five_points():
    assert update_score(0, "Too High", 2) == -5
    assert update_score(0, "Too Low", 3) == -5


def test_first_try_win_scores_100_points():
    assert update_score(0, "Win", 1) == 100


def test_invalid_text_is_rejected():
    assert parse_guess("not-a-number") == (False, None, "That is not a number.")
