def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a difficulty setting."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse a text guess and return (ok, value, error_message)."""
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw.strip())
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> str:
    """Return the logical outcome of comparing a guess with the secret."""
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def get_hint_message(outcome: str) -> str:
    """Return the user-facing hint for a comparison outcome."""
    messages = {
        "Win": "🎉 Correct!",
        "Too High": "📈 Go LOWER!",
        "Too Low": "📉 Go HIGHER!",
    }
    return messages.get(outcome, "")


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update score: reward a win and penalize each incorrect valid guess."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    return current_score
