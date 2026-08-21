gender = input('Enter gender (M/F):')
age = int(input('Enter the Age:'))

if(gender == 'F'):
        if(age >= 18):
            print('Girl is eligible for Marriage.')
        else:
            print('Girl is not eligible for Marriage.')
else: 
    if(age >= 21):
          print('Boy is eligible for Marriage.')
    else:
          print('Boy is not eligible for Marriage.')
          