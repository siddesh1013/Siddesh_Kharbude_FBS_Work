# 7. Write a program to solve the following series : b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n = int(input("Enter the value of n: "))
series_sum = 0

for i in range(1, n + 1):
    series_sum += n ** i

print("The sum of the series is:", series_sum)