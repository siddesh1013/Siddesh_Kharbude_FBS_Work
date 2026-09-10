# 5. WAP to print Fibonacci series upto n.

n = int(input("Enter a number: "))
a, b = 0, 1
print(f"Fibonacci series up to {n} is:")
while a <= n:
    print(a, end=' ')
    a, b = b, a + b