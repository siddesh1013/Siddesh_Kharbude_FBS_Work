def check_perfect(number):
	total = 0

	for divisor in range(1, number):
		if number % divisor == 0:
			total = total + divisor

	if total == number:
		return True
	else:
		return False


number = int(input('Enter a number: '))
res = check_perfect(number)
print(res)
