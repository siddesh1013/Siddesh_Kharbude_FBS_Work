# Write a program to calculate area of circle using function only

def calculate_area(radius):
    pi = 3.14
    return pi * radius ** 2

radius = int(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print("Area of the circle:", area)