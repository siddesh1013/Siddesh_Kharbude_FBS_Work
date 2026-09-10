# A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

total_price = 0
for i in range(5):
    price = int(input(f'Enter the price of product {i + 1}: '))
    total_price += price

gst = total_price * 0.18
total_bill = total_price + gst
print('Total bill after adding GST:', total_bill)