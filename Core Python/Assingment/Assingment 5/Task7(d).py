#Write a program to solve the following series : d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter the value of a: "))
series_sum = 0

for i in range(1, 11):
    series_sum += (a ** i) / i

print("The sum of the series is:", series_sum)