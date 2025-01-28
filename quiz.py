def ask_question(question, options, correct_answer):
    # This function asks the user a question and checks if the answer is correct.
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    answer = int(input("Enter the number of your answer: "))
    if options[answer - 1] == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")
        return 0

def play_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Paris", "Madrid", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is the capital of Kenya?",
            "options": ["Kigali", "Kampala", "Nairobi", "Dodoma"],
            "correct_answer": "Nairobi"
        },
        {
            "question": "Who directed the movie Inception?",
            "options": ["Christopher Nolan", "Steven Spielberg", "Martin Scorsese", "James Cameron"],
            "correct_answer": "Christopher Nolan"
        },
        {
            "question": "Which one of the following is not a Python data type?",
            "options": ["list", "tuple", "set", "table"],
            "correct_answer": "table"
        }
    ]
    score = 0
    for question in questions:
        score += ask_question(question['question'], question['options'], question['correct_answer'])
    
    print(f"Your final score is {score}/{len(questions)}.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ["yes", "y"]:
        play_quiz()

# Start the quiz
play_quiz()