def check_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


number = int(input('Enter a number: '))
res = check_prime(number)
print(res)