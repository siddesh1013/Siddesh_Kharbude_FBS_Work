### Write a program to check if user has entered correct userid and password.

correct_userid = "admin"
correct_password = "password123"

user_id = input("Enter your user ID: ")
password = input("Enter your password: ")

if user_id == correct_userid and password == correct_password:
    print("Login successful.")
else:
    print("Invalid user ID or password.")

    