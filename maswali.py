import json


def ask_questions(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    try:
        answer = int(input("Enter the number of your answer: "))
        if options[answer - 1] == correct_answer:
            print("Correct!\n")
            return 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")
            return 0
    except (ValueError, IndexError):
        print("Invalid input. Please try again.\n")
        return 0


def play_quiz():
    with open("questions.json", "r") as file:
        questions = json.load(file)

    while True:
        score = 0
        for question in questions:
            score += ask_questions(
                question["question"], question["options"], question["correct_answer"]
            )

        print(f"Your final score is {score}/{len(questions)}.")

        # Replay logic
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ["yes", "y"]:
                break  # Restart the quiz
            elif play_again in ["no", "n"]:
                print("Thank you for participating in the quiz!")
                return  # Exit the function
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


# Start the quiz
play_quiz()
