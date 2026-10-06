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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
