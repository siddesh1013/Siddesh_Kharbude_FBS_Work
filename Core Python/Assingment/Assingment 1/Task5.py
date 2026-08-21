### Write a program to enter P, T, R and calculate Compound Interest.

#Take Input
Principal_amount = int(input('Enter Principal Amount:'))
Time_Years = int(input('Enter Time in Years:'))
Rate_of_Interest = int(input('Enter Rate of Interest:'))

#Perform Further Calculation
Compound_Interest = Principal_amount * ((1 + Rate_of_Interest / 100) ** Time_Years)

#Display Result
print(f'Compound Interest: {Compound_Interest}')