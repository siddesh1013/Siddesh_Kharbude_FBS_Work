def check_perfect():
	number = int(input('Enter a number: '))
	total = 0

	for divisor in range(1, number):
		if number % divisor == 0:
			total = total + divisor

	if total == number:
		return True
	else:
		return False


print(check_perfect())

