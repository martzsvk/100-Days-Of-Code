# Day 37: Habit Tracker (Pixela API with Custom GUI) 📊

A personal habit tracking application that visualizes progress using the Pixela API. While the course focused on console-based requests, I developed a custom Graphical User Interface (GUI) to make the tool more user-friendly and practical for daily use.

## What I Learned 🛠️
* **Advanced HTTP Methods:** Moving beyond simple `GET` requests to master `POST` (creating data), `PUT` (updating data), and `DELETE` (removing data).
* **API Headers & Security:** Using HTTP Headers (`X-USER-TOKEN`) for authentication instead of URL parameters, which is a more secure and professional approach.
* **Separation of Concerns:** Structuring the project into two files (`main.py` for API logic and `app.py` for the UI) to maintain clean, scalable code.
* **Dynamic Centering:** Implementing logic to calculate screen dimensions and automatically center the application window on any monitor.

## How it Works ⚙️
1. The app launches a custom dark-themed GUI (Momiji/Burgundy style).
2. The user enters the number of minutes spent programming.
3. Upon clicking "Submit", the script fetches the current date and sends a `POST` request to the Pixela API.
4. The habit progress is updated on the user's personal Pixela heatmap (graph).
