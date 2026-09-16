# Write a program to find sum of following series using functions:
# a. 1 + 2 + 3 + 4 + ..... + n
# b. 1! + 2! + 3! + 4! + ..... + n!
# c. 1^1 + 2^2 + 3^3 + ..... + n^n

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

def sum_of_series(n):
    sum1 = 0
    sum2 = 0
    sum3 = 0

    for i in range(1, n + 1):
        sum1 += i
        sum2 += factorial(i)
        sum3 += i ** i

    return sum1, sum2, sum3

n = int(input("Enter a number: "))
a, b, c = sum_of_series(n)

print("Sum of series a:", a)
print("Sum of series b:", b)
print("Sum of series c:", c)