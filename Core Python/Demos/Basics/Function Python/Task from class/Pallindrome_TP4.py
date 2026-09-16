def check_palindrome(number):
	reverse = ''

	for digit in number:
		reverse = digit + reverse

	if number == reverse:
		return True
	else:
		return False


number = input('Enter a number: ')
res = check_palindrome(number)
print(res)
