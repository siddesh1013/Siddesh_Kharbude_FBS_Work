# Write a program to check if entered number is a palindrome or not using function only

def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original_num == reversed_num

n = int(input("Enter a number: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")