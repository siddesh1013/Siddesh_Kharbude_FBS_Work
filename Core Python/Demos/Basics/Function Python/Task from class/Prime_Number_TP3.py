def check_prime():
    number = int(input('Enter a number: '))

    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


res = check_prime()
print(res)