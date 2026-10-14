#STUDENT DATA ENTRY

# ask user for number of students
number_of_students = int(input("Enter number of students: "))

students = []

# ask each student for name and grade in a subject
for i in range(number_of_students):
    firstname = input("Enter student's firstname: ")
    lastname = input("Enter student's lastname: ")

    # creation of a list that stores the student's grades
    grades = []

    # Math grade
    grade = float(input("Enter Math grade (0-100): "))

    while grade <0 or grade >100:
        print("Invalid grade. Please enter a valid grade. ")
        grade = float(input("Enter Math grade (0-100): "))

    grades.append(grade)

    # English grade
    grade = float(input("Enter English grade (0-100): "))

    while grade < 0 or grade > 100:
        print("Invalid grade. Please enter a valid grade. ")
        grade = float(input("Enter English grade (0-100): "))

    grades.append(grade)

    # Science grade
    grade = float(input("Enter Science grade (0-100): "))

    while grade < 0 or grade > 100:
        print("Invalid grade. Please enter a valid grade. ")
        grade = float(input("Enter Science grade (0-100): "))

    grades.append(grade)

    # creation of a tuple with student names and grades
    student = ((firstname, lastname), grades)

    #add students to the students list
    students.append(student)

# STUDENT RECORDS DISPLAY
print("Student Summary")
print("-" * 70)

print(f"{'Name':<20}{'Math':<10}{'English':<10}{'Science':<10}{'Average':<10}")
print("-" * 70)

for student in students:
    firstname = student[0][0]
    lastname = student[0][1]
    grades = student[1]

    # student's average calculation
    student_average = sum(grades) / len(grades)

    name = firstname + " " + lastname

    print(f"{name:<20}{grades[0]:<10.1f}{grades[1]:<10.1f}{grades[2]:<10.1f}{student_average:<10.1f}")



# Highest and lowest grades for each subject
math_grades = []
english_grades = []
science_grades = []

for student in students:
    grades = student[1]

    math_grades.append(grades[0])
    english_grades.append(grades[1])
    science_grades.append(grades[2])

print("Highest and lowest Grades")

print("Math:")
print("Highest grade:", max(math_grades))
print("Lowest grade:", min(math_grades))

print("English:")
print("Highest grade:", max(english_grades))
print("Lowest grade:", min(english_grades))

print("Science:")
print("Highest grade:", max(science_grades))
print("Lowest grade:", min(science_grades))




