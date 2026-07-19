'''Riya is planning a movie night out with her friends. She loves watching movies, 
and she's always on the lookout for discounts to make the experience even better.
Riya discovered a local cinema offering discounts based on the day of the week and the number of tickets purchased.
Here's how the discount works:
On Mondays, if Riya buys 5 or more tickets, she gets a discount of Rs. 150 off the total price.
On other days, there are no specific discounts available.
write a program to help Riya calculate the total amount she needs to pay for the movie tickets based on the day of the
week and the number of tickets she intends to buy.
Note: Assume that the price of each ticket is Rs. 200/-'''

day = input().strip()
num_tickets = int(input())
ticket_price = 200
total_price = ticket_price * num_tickets
if day.lower() == 'monday' and num_tickets  >= 5:
    total_price -= 150
print("Total amount to be paid:",total_price)