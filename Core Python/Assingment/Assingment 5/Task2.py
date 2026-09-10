# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

num_students = int(input("Enter number of students: "))
total_percentage = 0

for student in range(1, num_students + 1):
    print("Enter marks for student", student, ":")
    total_marks = 0
    for subject in range(1, 6):
        marks = int(input("Subject " + str(subject) + ": "))
        total_marks += marks
    percentage = (total_marks / 500) * 100
    total_percentage += percentage
    print("Student", student, "percentage:", percentage, "%")

if num_students > 0:
    average_percentage = total_percentage / num_students
    print("Average percentage:", average_percentage, "%")
else:
    print("No students entered.")