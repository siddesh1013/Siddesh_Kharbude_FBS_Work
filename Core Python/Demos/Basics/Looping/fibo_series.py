num = int(input('How many fibonacci number do you want:'))

a = -1  # this must be initialized outside the loop otherwise it will always print 1 as the first number in the series.
b = 1

for i in range(num):
    c = a + b
    print(c, end = ' ')
    a = b
    b = c