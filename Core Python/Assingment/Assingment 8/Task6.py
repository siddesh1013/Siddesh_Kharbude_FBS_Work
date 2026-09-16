#  Write a program to find print the following Fibonacci series using functions: 1 1 2 3 5 8 n terms using function only

def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(b)
        a, b = b, a + b
    return fib_series

n = int(input("Enter the number of terms: "))
result = fibonacci_series(n)
print("Fibonacci series:", result)
