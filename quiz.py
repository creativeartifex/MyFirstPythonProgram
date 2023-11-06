# Python Quiz Game

def run_quiz():
    questions = [
        "What is the capital of France?",
        "Which data type is mutable in Python?",
        "What keyword is used to define a function in Python?"
    ]
    options = [
        ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        ["A) List", "B) Tuple", "C) String", "D) Integer"],
        ["A) function", "B) def", "C) create", "D) make"]
    ]
    correct_answers = ['B', 'A', 'B']
    score = 0

    for i in range(len(questions)):
        print(questions[i])
        for option in options[i]:
            print(option)
        answer = input("Enter (A, B, C, or D): ").upper()
        if answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print()

    print(f"You got {score} out of {len(questions)} correct!")


# Start the quiz
run_quiz()
