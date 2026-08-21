### Write a program to reverse three-digit number.

# Take Input
number = int(input("Enter a three-digit number: "))

# Reverse the number
reversed_number = (number % 10) * 100 + ((number // 10) % 10) * 10 + (number // 100)

# Display result
print("The reversed number is:", reversed_number)