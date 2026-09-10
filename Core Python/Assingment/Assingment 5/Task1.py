# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

userid = input("Enter UserID: ")
password = input("Enter Password: ")

for i in range(3):
    if userid == "admin" and password == "password123":
        print("Login successful!")
        break
    else:
        print("Incorrect UserID or Password. Please try again.")
        if i < 2:
            userid = input("Enter UserID: ")
            password = input("Enter Password: ")
            
print("Maximum attempts reached. Program terminated.")