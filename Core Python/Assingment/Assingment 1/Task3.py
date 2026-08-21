### Program to find quotient and remainder of two numbers.

# Take input from the user
dividend = int(input('Enter the dividend: '))
divisor = int(input('Enter the divisor: '))

# Find quotient and remainder
quotient = dividend // divisor
remainder = dividend % divisor

# Display the results
print(f'Quotient: {quotient}')
print(f'Remainder: {remainder}')