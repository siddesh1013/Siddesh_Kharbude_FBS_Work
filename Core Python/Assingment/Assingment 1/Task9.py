### Write a program to enter base and height of a triangle and find its area.

# Take input
base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))

# Perform calculation
Area = 1/2 * base * height

# Display the result
print(f'The area of the triangle with base {base} and height {height} is: {Area}')