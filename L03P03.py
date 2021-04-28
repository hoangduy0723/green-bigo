min_grade = 11
max_grade = -2
while (1 < 2):
    grade = int(input())
    if (grade == -1):
        break
    if (grade < min_grade):
        min_grade = grade
    if (grade > max_grade):
        max_grade = grade
print(max_grade, min_grade, end=' ')