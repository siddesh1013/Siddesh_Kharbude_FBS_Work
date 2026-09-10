### Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input("Enter the first angle of the triangle: "))
angle2 = int(input("Enter the second angle of the triangle: "))
angle3 = int(input("Enter the third angle of the triangle: "))

# Check if the sum of angles is 180 degrees
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")