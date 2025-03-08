import random
import os

def get_high_score():
    """Retrieve the high score from the file."""
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read().strip())
    return 0  # Default high score

def save_high_score(score):
    """Save a new high score to the file."""
    with open("highscore.txt", "w") as file:
        file.write(str(score))

# Load high score at the start
high_score = get_high_score()
score = 0  # Initialize current game score

print(f"🎯 Welcome to the Math Game! The current high score is: {high_score} 🎯\n")

while True:
    num1 = random.randint(1, 101)
    num2 = random.randint(1, 101)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    # Handle non-integer inputs
    while True:
        try:
            player_answer = int(input(f"What is {num1} {operation} {num2}? "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    if correct_answer == player_answer:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {correct_answer}.")

    print(f"Your current score: {score}")

    if score > high_score:
        print(f"🎉 Congrats! You've set a new high score: {score} (Previous: {high_score})")
        save_high_score(score)

    play_again = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if play_again == "no":
        print(f"\nGame Over! Final Score: {score} | High Score: {get_high_score()}")
        break