### Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))
if 100 <= num <= 999:

    num_str = str(num)
    if num_str == num_str[::-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

else:
    print("Please enter a valid 3-digit number.")