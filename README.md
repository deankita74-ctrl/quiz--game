🎮 Smart Quiz Game (Python CLI Project)

📌 Overview

Smart Quiz Game is a command-line based Python application designed to test users' knowledge through multiple-choice questions. The game supports different difficulty levels, timed responses, and score tracking, making it both engaging and interactive.

This project demonstrates core programming concepts such as modular design, file handling, user input validation, and basic game logic.

---

✨ Features

- 🧠 Multiple-choice quiz system
- ⏱️ Time-limited answering (10 seconds per question)
- 🎯 Difficulty levels: Easy, Medium, Hard
- 🔀 Random question selection
- 📊 Score calculation with accuracy percentage
- 💾 Persistent score storage in a file
- 🔁 Replay option after quiz completion

---

🛠️ Technologies Used

- Python 3
- Standard Libraries:
  - "random"
  - "time"
  - File Handling (".txt" storage)

---

📂 Project Structure

quiz-game/
│── main.py          # Entry point of the application
│── quiz_logic.py    # Handles question flow and validation
│── questions.py     # Stores quiz questions categorized by difficulty
│── utils.py         # Utility functions (timer + score saving)
│── scores.txt       # Stores user scores
│── README.md        # Project documentation

---

▶️ How to Run the Project

1️⃣ Prerequisites

Make sure Python is installed on your system:

python --version

2️⃣ Run the Game

python main.py

---

🎯 How It Works

1. User enters their name
2. Selects difficulty level
3. System randomly selects questions
4. Each question must be answered within 10 seconds
5. Score is calculated and displayed
6. Score is saved to "scores.txt"
7. User can choose to replay

---

📊 Output (VS Code Terminal)

PS C:\Users\Ankita\quiz-game> python main.py

🎮 Welcome to Smart Quiz Game!
Enter your name: Ankita

Choose difficulty (easy/medium/hard): medium

🚀 Starting Quiz...


Question 1/5
Capital of India?
1. Mumbai
2. Delhi
3. Kolkata
4. Chennai
You have 10 seconds to answer:
Your answer (1-4): 2
✅ Correct!


Question 2/5
5 * 6 = ?
1. 30
2. 25
3. 20
4. 35
You have 10 seconds to answer:
Your answer (1-4): 1
✅ Correct!


Question 3/5
Largest ocean?
1. Atlantic
2. Indian
3. Pacific
4. Arctic
You have 10 seconds to answer:
Your answer (1-4): 3
✅ Correct!


📊 Quiz Completed!
✅ Score: 3/3
📈 Accuracy: 100.00%

Play again? (yes/no): no
👋 Thank you for playing!

---

🚀 Future Enhancements

- 🖥️ GUI version using Tkinter or PyQt
- 🌐 Web-based version using Flask
- 🏆 Leaderboard system (Top scores)
- 📦 Database integration (SQLite / MySQL)
- 🔐 User login system

---

📌 Learning Outcomes

This project helps in understanding:

- Modular programming in Python
- Input handling and validation
- File operations
- Basic game development logic
- Structuring real-world projects

---

🤝 Contribution

Contributions are welcome!
Feel free to fork this repository, improve the code, and submit a pull request.

---

📄 License

This project is open-source and available under the MIT License.

---

👩‍💻 Author

Developed by Ankita De

---

🌟 Support

If you found this project useful, consider giving it a ⭐ on GitHub
