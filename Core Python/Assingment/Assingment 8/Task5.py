# Sum of all prime numbers between 1 to n using function

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_prime_numbers(n):
    sum_prime = 0
    for i in range(2, n + 1):
        if is_prime(i):
            sum_prime += i
    return sum_prime

n = int(input("Enter a number: "))
result = sum_of_prime_numbers(n)
print("Sum of prime numbers:", result)