### WAP to calculate area of triangle and rectangle.

# Take Input for Rectangle
length = float(input('Enter length of rectangle: '))
width = float(input('Enter width of rectangle: '))

# Calculate Area of Rectangle
area_rectangle = length * width

# Display Result for Rectangle
print(f'Area of rectangle with length {length} and width {width} is {area_rectangle}.')

# Take Input for Triangle
base = float(input('Enter base of triangle: '))
height = float(input('Enter height of triangle: '))

# Calculate Area of Triangle
area_triangle = 0.5 * base * height

# Display Result for Triangle
print(f'Area of triangle with base {base} and height {height} is {area_triangle}.')