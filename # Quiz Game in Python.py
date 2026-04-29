# Quiz Game in Python

def quiz_game():
    score = 0

    # Questions and answers
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "2. Which language is used for Python?",
            "options": ["A. HTML", "B. Java", "C. Python", "D. C++"],
            "answer": "C"
        },
        {
            "question": "3. What is 5 + 3?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "answer": "C"
        },
        {
            "question": "4. Who developed Python?",
            "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
            "answer": "C"
        }
    ]

    # Loop through questions
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! Correct answer is", q["answer"])

    # Final score
    print("\n🎉 Quiz Completed!")
    print("Your Score:", score, "/", len(questions))


# Run the game
quiz_game()