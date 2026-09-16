n = 5

for i in range(1, n + 1):

    if i == 1:
        for j in range(1, n + 1):
            print(j, end=" ")

    elif i == n:
        print(i, end=" ")

    else:
        print(i, end=" ")

        for j in range(n - i - 1):
            print(" ", end=" ")

        print(n, end=" ")

    print()