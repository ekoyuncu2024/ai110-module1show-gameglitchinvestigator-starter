# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game opened normally and let me choose a difficulty and enter guesses, but its behavior quickly became inconsistent. When the secret number was 82, I entered a very large negative number and the game told me to go lower even though the correct direction was higher. The attempt counter was also off: the page still showed one attempt left while simultaneously reporting that I was out of attempts. After losing, clicking New Game reset the displayed attempt count to eight, but the game still said "Game over. Start a new game to try again," so it was not actually playable again.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Entered a very large negative number while the secret was 82 | The hint should tell me to go higher | The game displayed "Go LOWER!" | none |
| Submitted the final wrong guess on Normal difficulty | The game-over message and attempts-left display should agree that no attempts remain | The game said "Out of attempts!" while the page still showed "Attempts left: 1" | none |
| Clicked **New Game** after losing | A fresh game should start and accept guesses | The attempt count reset to 8, but the app still displayed "Game over. Start a new game to try again." | none |

---

## 2. How did you use AI as a teammate?

I used ChatGPT as the AI coding assistant for the entire debugging process. One correct suggestion was to move the reusable game rules out of `app.py` and into `logic_utils.py`, then test those functions directly with pytest; after the refactor, all seven tests passed and the repaired behavior also worked in the live Streamlit app. I did not accept every possible cleanup as necessary: extra UI polish and unrelated feature changes would have made the project larger without helping reproduce or fix the three bugs I actually observed. I kept the repair focused on the documented glitches and verified the result by running both pytest and the live game.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after the corrected behavior worked in both an automated test and the running Streamlit app. For example, the regression test for a very low guess against a secret of 82 checks that the logical outcome is "Too Low" and that the displayed hint tells the player to go higher. I ran `python3 -m pytest` on my Mac and all seven tests passed in 0.02 seconds. ChatGPT helped design the regression tests around the exact bugs that were reproduced before the code was changed.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python script from top to bottom whenever the user interacts with a widget, so normal local variables do not automatically represent a persistent game. `st.session_state` is the place to keep values that must survive those reruns, such as the secret number, score, attempt count, game status, and history. I also learned that resetting a game means resetting all related state together; changing only the secret or attempt count can leave the app in an old won/lost state. Using a single reset function made that behavior much easier to reason about.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is reproducing a bug first, writing down the expected and actual behavior, and then adding a regression test for the exact failure before considering the repair complete. I also want to keep using small, meaningful Git commits so the debugging history is easy to follow instead of making one large commit at the end. Next time I use AI for coding, I would give it one clearly reproduced bug at a time and require a test that proves each proposed fix. This project made me treat AI-generated code as a starting point that still needs direct verification rather than assuming that code is correct because it looks reasonable.
