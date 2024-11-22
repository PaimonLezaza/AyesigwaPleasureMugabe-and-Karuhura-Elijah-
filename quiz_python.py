import random

questions = [
    {"question": "What is the capital city of Uganda?", "options": ["Kampala", "Entebbe", "JinJa"], "answer": "Kampala"},
    {"question": "What is the capital city of USA?", "options": ["New York", "Chicago", "Washington, D.C"], "answer": "Washington, D.C"},
    {"question": "What is the capital city of Rwanda?", "options": ["Kigali", "Rutoma", "Kishasha"], "answer": "Kigali"},
    {"question": "What is the longest river in Africa?", "options": ["R.Nile", "R.Aswa", "R.Rwizi"], "answer": "R.Nile"},
    {"question": "Which of the following is the smallest unit of data in a computer?", "options": ["Byte", "Bit", "Kilobyte"], "answer": "Bit"},
    {"question": "Which of the following programming languages is primarily used for web development?", "options": ["HTML", "Python", "CSS"], "answer": "HTML"}
]

random.shuffle(questions)
score = 0

print("Welcome to The Quiz Game")
for i, q in enumerate(questions):
    print(f"Question {i + 1}: {q['question']}")    
    for index, option in enumerate(q['options'], start=1):
        print(f"{index}. {option}")
    while True:
        answer = input("Enter the number of your answer: ")        
        if answer.isdigit():
            answer_num = int(answer)            
            if 1 <= answer_num <= len(q['options']):
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(q['options'])}.")
        else:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")
    if q['options'][answer_num - 1] == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {q['answer']}")
print(f"Your final score is: {score}/{len(questions)}")
if score == len(questions):
    print("Excellent! You're a genius!")
elif score > len(questions) // 2:
    print("Good job! You did well.")
else:
    print("Better luck next time.")
