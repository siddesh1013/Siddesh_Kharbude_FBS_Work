### Write a program to swap two numbers without using third variable.

# Take Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform Swap without using a third variable
num1, num2 = num2, num1

# Display Result
print("After swapping, the first number is:", num1)
print("After swapping, the second number is:", num2)