### Write a program to enter P, T, R and calculate simple Interest.

#Take Input
Principal_amount = int(input('Enter Principal Amount:'))
Time_Years = int(input('Enter Time in Years:'))
Rate_of_Interest = int(input('Enter Rate of Interest:'))

#Perform Further Calculation
Simple_Interest = (Principal_amount * Time_Years * Rate_of_Interest) / 100

#Display Result
print(f'Simple Interest: {Simple_Interest}') 