marks = int(input("Enter your score: "))


if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 80 and marks <= 89:
    grade = "B"
elif marks >= 70 and marks <= 79:
    grade = "C"
elif marks >= 60 and marks <= 69:
    grade = "D"
elif marks >= 50 and marks <= 59:
    grade = "E"
elif marks >= 40 and marks <= 49:
    grade = "E-"
elif marks < 40:
    grade = "F (Fail)"
else:
    grade = "Invalid score"


print("Grade:", grade)