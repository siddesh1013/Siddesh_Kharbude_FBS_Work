rows = 10
width = 22

for i in range(rows):
    if i == 0 or i == rows - 1:
        print('*' * width)
    else:
        position = width - 1 - round(i * (width - 1) / (rows - 1))
        print(' ' * position + '*')