def check_palindrome():
	number = input('Enter a number: ')
	reverse = ''

	for digit in number:
		reverse = digit + reverse

	if number == reverse:
		return True
	else:
		return False


print(check_palindrome())
