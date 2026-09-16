def check_armstrong(number):
	original_number = number
	number_of_digits = len(str(number))
	total = 0

	while number > 0:
		digit = number % 10
		total = total + digit ** number_of_digits
		number = number // 10

	if total == original_number:
		return True
	else:
		return False


number = int(input('Enter a number: '))
print(check_armstrong(number))
