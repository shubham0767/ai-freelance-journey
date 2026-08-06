from functools import reduce

print("=" * 50)
print("Student Marks Analyzer")
print("=" * 50)

marks = [45, 60, 72, 30, 88, 95, 40]

passed = [mark for mark in marks if mark >= 35]

grace_marks = list(map(lambda x: x + 5, marks))

top_scorers = list(filter(lambda x: x > 75, marks))

total = reduce(lambda x, y: x + y, marks)

print("Original Marks :", marks)
print("Passed Students :", passed)
print("Grace Marks List:", grace_marks)
print("Top Scorers     :", top_scorers)
print("Total Marks     :", total)