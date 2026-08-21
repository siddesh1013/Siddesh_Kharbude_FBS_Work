### Write a Program to input two angles from user and find third angle of the triangle.

# Take input 
angle1 = int(input('Enter first angle of triangle:'))
angle2 = int(input('Enter second angle of triangle:'))

# Perform calculation
angle3 = 180 - (angle1 + angle2)

# Display the result
print('The third angle of the triangle is:', angle3)