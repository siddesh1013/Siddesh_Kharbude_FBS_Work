### Find the sum of three-digit number.

# Take Input
number = int(input("Enter a three-digit number: "))

# Calculate the sum of digits
sum_of_digits = number // 100 + (number // 10) % 10 + number % 10

# Output the result
print("The sum of the digits is:", sum_of_digits)
