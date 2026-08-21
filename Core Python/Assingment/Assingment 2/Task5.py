### WAP to calculate selling price of book based on cost price and discount.

# Take Input
cost_price = int(input("Enter the cost price of the book: "))
discount = int(input("Enter the discount percentage: "))

# Calculate Selling Price
selling_price = cost_price - (cost_price * discount / 100)

# Display Result
print("The selling price of the book is:", selling_price)