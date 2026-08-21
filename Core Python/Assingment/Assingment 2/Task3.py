### Convert distant given in feet and inches into meter and centimeter.

# Take input
feet = float(input('Enter feet: '))
inches = float(input('Enter inches: '))

# Perform calculation
total_inches = feet * 12 + inches
meters = total_inches * 0.0254
centimeters = meters * 100

# Display the result
print(f'Distance in meters: {meters}')
print(f'Distance in centimeters: {centimeters}')