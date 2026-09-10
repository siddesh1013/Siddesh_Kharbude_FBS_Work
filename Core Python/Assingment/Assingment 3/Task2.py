### Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter any alphabet: ")
if len(alphabet) == 1 and alphabet.isalpha():
    if alphabet.lower() in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a single alphabet character.")