### Input 5 subject marks from user and display grade(eg.First class,Second class ..)

marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total_marks = sum(marks)
average = total_marks / 5

if average >= 80:
    grade = "First Class"
elif average >= 60:
    grade = "Second Class"
elif average >= 40:
    grade = "Third Class"
else:
    grade = "Fail"

print(f"Total Marks: {total_marks}")
print(f"Average: {average}")
print(f"Grade: {grade}")