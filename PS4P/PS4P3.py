num_books = int(input("Enter the number of books to order: "))
cost_per_book = float(input("Enter the cost per book: "))

total_cost = num_books * cost_per_book

ship_charge = 25 if total_cost <= 50 else 0

order_total = total_cost + ship_charge
print("Order total: $", order_total)
print("Shipping charge: $", ship_charge)