# WAP to print all odd numbers until n.

n = int(input("Enter a number: "))
print(f"Odd numbers from 1 to {n} are:")
for i in range(1, n + 1, 2):
    print(i, end=' ')