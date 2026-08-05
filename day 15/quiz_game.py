print("=" * 40)
print("Python Quiz")
print("=" * 40)

score = 0

questions = [
    ("What is the capital of India?", "B", ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"]),
    ("Which language are we learning?", "C", ["A. Java", "B. C++", "C. Python", "D. PHP"]),
    ("How many days are there in a week?", "B", ["A. 5", "B. 7", "C. 8", "D. 10"]),
    ("Which planet is known as the Red Planet?", "A", ["A. Mars", "B. Earth", "C. Venus", "D. Jupiter"]),
    ("How many months are there in a year?", "D", ["A. 10", "B. 11", "C. 13", "D. 12"])
]


for question, answer, options in questions:
    print("\n"+ question)
    for option in options :
        print(option)

    user =input("enter answer:").upper()

    if user == answer:
        score+=1


percentage=(score/len(questions))*100
print("\nCorrect Answers :", score)
print("Score :", percentage, "%")