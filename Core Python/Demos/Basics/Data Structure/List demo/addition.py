li = [10, 20, 30, 40, 50, 60, 70]

sum = 0

#1. Method: Iterarting values
# for ele in li:
#     sum += ele
# print(sum)

#2. Method: Using indexing
for ind in range(0, len(li)):
    sum += li[ind]

print(sum)


#3. WAA to find out maximum elemnet from your list eg: li = [40, 20, 60, 30, 50, 10]