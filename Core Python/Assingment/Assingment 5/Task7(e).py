# Write a program to solve the following series : e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))
series_sum = 0

for i in range(1, n + 1):
    term = (x ** i) / (2 * i - 1)
    if i % 2 == 0:
        series_sum -= term
    else:
        series_sum += term

print("The sum of the series is:", series_sum)