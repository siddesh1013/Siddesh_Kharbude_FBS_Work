### Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user):

length = int (input("Enter length: "))
breadth = int (input("Enter breadth: "))
radius = int (input("Enter radius: "))

pi = 3.14

# Area of rectangle
area_rectangle = length * breadth

# Area of semicircle
area_semicircle = (pi * radius * radius) / 2

# Total area
area = area_rectangle + area_semicircle

# Perimeter
perimeter = (2 * length) + breadth + (pi * radius)

print("Area =", area)
print("Perimeter =", perimeter)