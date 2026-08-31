### Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

Principal_amount = int(input('Enter Principal Amount:'))
Time_Years = int(input('Enter Time in Years:'))
Rate_of_Interest = int(input('Enter Rate of Interest:'))

Simple_Interest = (Principal_amount * Time_Years * Rate_of_Interest) / 100

print(f'Simple Interest: {Simple_Interest}')