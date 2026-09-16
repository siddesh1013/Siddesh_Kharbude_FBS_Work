# Sum of all odd numbers between 1 to n using function

def sum_of_odd_numbers(n):
    sum_odd = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum_odd += i
    return sum_odd

n = int(input("Enter a number: "))
result = sum_of_odd_numbers(n)
print("Sum of odd numbers:", result)