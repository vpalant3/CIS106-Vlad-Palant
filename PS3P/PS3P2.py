purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = int(input("Enter the quantity of stock: "))

def compute_stock_value(purchase_price, current_price, quantity):
	return (current_price - purchase_price) * quantity

result = compute_stock_value(purchase_price, current_price, quantity)
print("Value change of the stock: $", result)