# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

This project is a Streamlit number-guessing game that started with several deliberate logic and state-management bugs. The goal was to reproduce the glitches, use AI-assisted debugging to repair them, refactor the core logic into testable functions, and verify the result with pytest and live testing.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run the tests: `python -m pytest`

## 🕵️‍♂️ What Was Broken

The initial version had several reproducible problems:

- The HIGHER/LOWER hints were reversed.
- The attempts-left display could disagree with the game-over state.
- Clicking **New Game** after losing did not fully reset the game status.
- The comparison logic could alternate between numeric and string versions of the secret.
- Core game logic was still embedded in `app.py` instead of being isolated for testing.

## 🔧 What Was Fixed

The reusable game rules were moved into `logic_utils.py`, including guess parsing, comparison logic, hint generation, difficulty ranges, and score updates. The Streamlit state reset was centralized so a new game resets the secret, attempts, score, status, history, and difficulty-specific state together. The hint direction and attempt-count behavior were corrected, and regression tests were added for the original failures.

## 📸 Demo Walkthrough

1. Start the app on **Normal** difficulty, which uses the range 1 to 100.
2. Open **Developer Debug Info** to view the secret number for testing.
3. Enter a guess below the secret; the game correctly responds **Go HIGHER!**
4. Enter a guess above the secret; the game correctly responds **Go LOWER!**
5. Enter the exact secret number; the game displays the win message and final score.
6. Click **New Game 🔁**; the attempts, score, history, game status, and secret reset correctly and the game is immediately playable again.
7. Change the difficulty to **Easy**; the displayed range changes to 1 to 20 and a new secret is generated inside that range.

## 🧪 Test Results

The repaired project was tested locally on macOS with Python 3.14.8 and pytest 9.1.1:

```text
============================= test session starts ==============================
platform darwin -- Python 3.14.8, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/emirkoyuncu/codepath-game/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 7 items

tests/test_game_logic.py .......                                         [100%]

============================== 7 passed in 0.02s ===============================
```

## 📝 AI-Assisted Development

ChatGPT was used as the AI coding assistant to inspect the starter code, identify the causes of the reproduced bugs, refactor the logic, create regression tests, and help document the debugging process. Each repair was checked against the observed behavior, and the final version was verified both with pytest and by running the Streamlit app manually.
