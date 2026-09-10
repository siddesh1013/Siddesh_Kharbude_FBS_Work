# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

num_passengers = int(input("Enter number of passengers: "))
ticket_cost = int(input("Enter per ticket cost: "))
total_amount = 0

for passenger in range(1, num_passengers + 1):
    age = int(input("Enter age of passenger " + str(passenger) + ": "))
    
    if age < 12:
        discount = 0.30 * ticket_cost
        final_cost = ticket_cost - discount
    elif age > 59:
        discount = 0.50 * ticket_cost
        final_cost = ticket_cost - discount
    else:
        final_cost = ticket_cost
    
    total_amount += final_cost

print("Total amount for all passengers:", total_amount)