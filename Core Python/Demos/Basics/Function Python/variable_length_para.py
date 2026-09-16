def addition(*num):
    sum = 0
    for value in num:
        sum += value
    return sum
res = addition(10,20,30,40,50)
print(res)