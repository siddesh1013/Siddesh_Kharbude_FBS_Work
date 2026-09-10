# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

correct_userid = "admin"
correct_password = "password123"

user_id = input("Enter your user ID: ")
password = input("Enter your password: ")

if user_id == correct_userid and password == correct_password:
    seed = sum(ord(character) for character in user_id + password)
    captcha = 1000 + (seed * 37 % 9000)

    print("CAPTCHA:", captcha)

    user_captcha = input("Enter the CAPTCHA: ")

    if user_captcha == str(captcha):
        print("Success! CAPTCHA verified.")
    else:
        print("Failed! Incorrect CAPTCHA.")
else:
    print("Invalid user ID or password.")