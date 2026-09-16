# Write a program find reverse of a number using function only

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

n = int(input("Enter a number: "))
result = reverse_number(n)
print("Reverse of the number is:", result)
