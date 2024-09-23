student_score = {
    "Ram": 57,
    "Shyam": 98,
    "Rita": 44,
    "Asmita": 82,
    "Pramita": 81
}

student_grade = {}

for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score >80:
        student_grade[student] = "Exceeds expectation"
    elif score > 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"

print(student_grade)