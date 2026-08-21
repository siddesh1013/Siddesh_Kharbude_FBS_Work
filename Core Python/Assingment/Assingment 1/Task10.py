### Write a program to calculate area of an equilateral triangle.

# Take input
side = float(input('Enter the length of a side of the equilateral triangle: '))

# Perform calculation
Area = (3 ** 0.5 / 4) * side ** 2

# Display the result
print(f'The area of the equilateral triangle with side {side} is: {Area}')