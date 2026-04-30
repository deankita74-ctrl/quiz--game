from utils import timer_input

def ask_question(q):
    print(q["question"])

    # Display options
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")

    # Get answer with timer
    answer = timer_input(10)

    # Time up case
    if answer is None:
        print(f"⏰ Time up! Correct answer is: {q['answer']}")
        return False

    try:
        answer = int(answer)

        # Check valid range
        if answer < 1 or answer > len(q["options"]):
            print(f"❌ Invalid choice! Correct answer is: {q['answer']}")
            return False

        # Check correct answer
        if q["options"][answer - 1] == q["answer"]:
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Wrong! Correct answer is: {q['answer']}")
            return False

    except:
        print(f"❌ Invalid input! Correct answer is: {q['answer']}")
        return False