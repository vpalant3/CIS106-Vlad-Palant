quantity = int(input("Enter the quantity of the item: "))
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = 0.07 * extended_price
total = extended_price + tax

print("Quantity:", quantity)
print("Unit Price: $", unit_price)
print("Extended Price: $", extended_price)
print("Tax: $", tax)
print("Total: $", total)