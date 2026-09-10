# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num = int(input('Enter the number: '))

temp = num
count = 0
while(temp > 0):
    count += 1
    temp = temp // 10

temp = num
sum = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    sum = sum + (d ** count)

if(sum == num):
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.' )