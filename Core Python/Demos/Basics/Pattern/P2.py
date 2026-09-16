# count=1
# for i in range(1, 6):
#     for j in range(1,6):
#         while(count<=i):
#             print('*'*i)
#             count+=1
#             print()

for i in range(1,6):
    for j in range(1, i + 1):
        print('*', end =' ')
    print()