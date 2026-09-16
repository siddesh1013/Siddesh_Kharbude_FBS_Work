def check_strong(number):
	original_number = number
	total = 0

	while number > 0:
		digit = number % 10
		factorial = 1

		for value in range(1, digit + 1):
			factorial = factorial * value

		total = total + factorial
		number = number // 10

	if total == original_number:
		return True
	else:
		return False


number = int(input('Enter a number: '))
print(check_strong(number))
