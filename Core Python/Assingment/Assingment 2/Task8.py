### Write a program to swap two numbers using third variable.

# Take Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perfrom Swap using a third variable
x = num1
num1 = num2
num2 = x

# Display Result
print("After swapping, the first number is:", num1)
print("After swapping, the second number is:", num2)
