student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 71,
}
# 🚨 Don't change the code above 👆


student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for grades in student_scores:
    if student_scores[grades] > 90:
        student_grades[grades] = "Outstanding"
    elif student_scores[grades] > 80:
        student_grades[grades] = "Exceeds Expectations"
    elif student_scores[grades] > 70:
        student_grades[grades] = "Acceptable"
    else:
        student_grades[grades] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)