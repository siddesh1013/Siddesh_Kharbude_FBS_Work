### WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

# Take Input
basic = int(input("Enter the basic salary of the employee: "))

# Calculate Allowances
da = basic * 0.10
ta = basic * 0.12
hra = basic * 0.15

# Calculate Total Salary
total_salary = basic + da + ta + hra

# Display Result
print("The total salary of the employee is:", total_salary)