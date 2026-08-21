### Program to Find the Roots of a Quadratic Equation.

#Take input
a = float(input('Enter the coefficient a: '))
b = float(input('Enter the coefficient b: '))
c = float(input('Enter the coefficient c: '))

# Perform calculation
d = (b**2) - (4*a*c)

# Determine the nature of the roots based on the discriminant
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print('The roots are real and different.')
    print('Root 1:', root1)
    print('Root 2:', root2)

elif d == 0:
    root = -b / (2*a)
    print('The roots are real and the same.')
    print('Root:', root)

else:
    realPart = -b / (2*a)
    imaginaryPart = (abs(d)**0.5) / (2*a)
    print('The roots are complex and different.')
    print('Root 1:', realPart, '+', imaginaryPart, 'i')
    print('Root 2:', realPart, '-', imaginaryPart, 'i')

# Display the discriminant
print('Discriminant:', d)