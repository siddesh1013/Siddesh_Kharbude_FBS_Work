### Write a program to convert days into years, weeks and days.

# Take input
days = int(input('Enter the number of days: '))

# Perform calculation
years = days // 365
remaining_days_after_years = days % 365
weeks = remaining_days_after_years // 7
remaining_days_after_weeks = remaining_days_after_years % 7

# Display the result
print(f'{days} days is equivalent to {years} years, {weeks} weeks, and {remaining_days_after_weeks} days.')
