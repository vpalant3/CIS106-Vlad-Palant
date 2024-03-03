num_tickets = int(input("Enter the number of concert tickets: "))

if num_tickets >= 25:
    price_per_ticket = 50
elif num_tickets >= 10:
    price_per_ticket = 60
elif num_tickets >= 5:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = num_tickets * price_per_ticket
print(f"Number of tickets: {num_tickets}")
print(f"Price per ticket: ${price_per_ticket}")
print(f"Total cost: ${total_cost}")