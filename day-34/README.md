# Day 34: GUI Quiz App 📝

Quiz Application that fetches random trivia questions from the Open Trivia Database API. This project focuses on class-based UI management and handling data updates in a GUI.

## What I Learned 🛠️
* **OOP Integration:** Connecting a `QuizBrain` logic class with a `UI` class to separate data processing from visual display.
* **API Unescaping:** Learning how to handle HTML entities in API strings (e.g., converting `&quot;` back into `"` using the `html` library).

## How it Works ⚙️
1. The app fetches 10 True/False questions from an external API.
2. The UI displays the question on a custom Tkinter Canvas.
3. The user clicks the Check or Cross button.
4. The app provides instant visual feedback (Green/Red).
5. Once 10 questions are answered, the game ends and shows the final score.

## Requirements 📦
* **Requests:** To fetch the trivia data.
* **HTML library:** To decode special characters in the questions.
* **Tkinter:** For the graphical interface.
