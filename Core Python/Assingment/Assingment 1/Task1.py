### Write a program to calculate the percentage of student based on marks of any 5
subjects

#Take Input
Subject1 = int(input('Enter marks for Subject 1:'))
Subject2 = int(input('Enter marks for Subject 2:'))
Subject3 = int(input('Enter marks for Subject 3:'))    
Subject4 = int(input('Enter marks for Subject 4:'))
Subject5 = int(input('Enter marks for Subject 5:'))

#Perform Further Calculation
total_marks = (Subject1 + Subject2 + Subject3 + Subject4 + Subject5) / 500 * 100

#Display Result
print(f'Total Marks: {total_marks} %')