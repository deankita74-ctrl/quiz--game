import time

def timer_input(timeout):
    print(f"You have {timeout} seconds to answer:")
    start = time.time()
    answer = input("Your answer (1-4): ")
    end = time.time()

    if end - start > timeout:
        return None
    return answer


def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name}: {score}\n")