num = int(input('Enter the number: '))

original = num
reverse = 0

while(num > 0):
    digit = num % 10
    num = num // 10
    reverse = reverse * 10 + digit
if (original == reverse):
    print('The number is Palindrome')
else:
    print('The number is not Palindrome')
