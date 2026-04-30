import random
from questions import questions
from quiz_logic import ask_question
from utils import save_score

def start_quiz():
    print("🎮 Welcome to Smart Quiz Game!")
    name = input("Enter your name: ")

    level = input("Choose difficulty (easy/medium/hard): ").lower()

    if level not in ["easy", "medium", "hard"]:
        print("Invalid difficulty!")
        return

    selected_questions = questions[level]

    if len(selected_questions) < 5:
        quiz_questions = selected_questions
    else:
        quiz_questions = random.sample(selected_questions, 5)

    score = 0
    total = len(quiz_questions)

    print("\n🚀 Starting Quiz...\n")

    for i, q in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {i}/{total}")
        if ask_question(q):
            score += 1

    print("\n📊 Quiz Completed!")
    print(f"✅ Score: {score}/{total}")

    accuracy = (score / total) * 100
    print(f"📈 Accuracy: {accuracy:.2f}%")

    save_score(name, score)

    replay = input("\nPlay again? (yes/no): ").lower()
    if replay == "yes":
        start_quiz()
    else:
        print("👋 Thank you for playing!")

if __name__ == "__main__":
    start_quiz()