### Convert the time entered in hh,min and sec into seconds.

# Take input
hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))
seconds = int(input('Enter seconds: '))

# Perform calculation
Total_seconds = hours * 3600 + minutes * 60 + seconds

# Display the result
print(f'The total time in seconds is: {Total_seconds}')