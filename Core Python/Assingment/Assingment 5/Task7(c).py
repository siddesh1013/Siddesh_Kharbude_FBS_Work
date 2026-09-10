# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter the value of n: "))
series_sum = 0
ratio = 2

for i in range(1, n + 1):
    series_sum += ratio ** i

print("The sum of the geometric series is:", series_sum)