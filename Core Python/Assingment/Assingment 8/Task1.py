# Write a program to calculate area of rectangle using function only

def calculate_area(length, width):
    return length * width

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print("Area of the rectangle:", area)
