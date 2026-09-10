### Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))

# Check if the sum of any two sides is greater than the third side
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")