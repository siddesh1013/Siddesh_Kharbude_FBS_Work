# Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter the value of n: "))
factorial = 1
series_sum = 0

for i in range(1, n + 1):
    factorial *= i
    series_sum += factorial

print("The sum of the series is:", series_sum)