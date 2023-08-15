quiz_questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Jupiter", "Saturn", "Mars"],
        "correct_answer": 1
    },
    {
        "question": "Who wrote the Harry Potter series?",
        "answers": ["J.K. Rowling", "Stephenie Meyer", "Suzanne Collins", "George R.R. Martin"],
        "correct_answer": 0
    },
    {
        "question": "What is the largest country in the world?",
        "answers": ["Russia", "Canada", "China", "United States"],
        "correct_answer": 0
    },
    {
        "question": "What is the largest ocean in the world?",
        "answers": ["Pacific", "Atlantic", "Indian", "Arctic"],
        "correct_answer": 0
    },
    {
        "question": "What is the largest animal in the world?",
        "answers": ["Blue Whale", "African Elephant", "Giraffe", "Brown Bear"],
        "correct_answer": 0
    },
    {
        "question": "What is the largest bird in the world?",
        "answers": ["Ostrich", "Emu", "Cassowary", "Albatross"],
        "correct_answer": 0
    },
    {
        "question": "What is the pH value of the human body?",
        "answers": ["9.2 to 9.8","7.0 to 7.8","6.1 to 6.3","5.4 to 5.6"],
        "correct_answer": 1
    },
    {
        "question": "Which of the given devices is used for counting blood cells?",
        "answers": ["Haemocytometer","Spectroscope","Stethoscope","Endoscope"],
        "correct_answer": 0
    },
    {
        "question": "Which of the given compounds is used to make fireproof clothing?",
        "answers": ["Aluminum chloride","Aluminum Sulphate","Magnesium Chloride","Magnesium Sulphate"],
        "correct_answer": 1
    }
]

score = 0

print("Welcome to the Quiz Game!")
print("You will be asked multiple-choice questions on a specific topic.")
print("For each question, enter the number of the answer you think is correct.")

for quiz_question in quiz_questions:
    print(quiz_question["question"])
    for i, answer in enumerate(quiz_question["answers"]):
        print(f"{i+1}: {answer}")
    user_answer = int(input("Enter your answer: "))
    if user_answer == quiz_question["correct_answer"]+1:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was: {quiz_question['answers'][quiz_question['correct_answer']]}")

print(f"You scored {score} out of {len(quiz_questions)}")

if score<4:
    print("Performation evaluation: Bad")
elif score>=4 and score<8:
    print("Performation evaluation: Average")
else:
    print("Performation evaluation: Good")