def calculate_price(quantity):
    if quantity > 10000:
        price = 10
    elif quantity >= 5000 and quantity <= 10000:
        price = 20
    else:
        price = 30

    extended_price = quantity * price
    tax_amount = extended_price * 0.07
    total = extended_price + tax_amount

    print(f"Extended Price: ${extended_price}")
    print(f"Tax Amount: ${tax_amount}")
    print(f"Total: ${total}")

# Example usage
calculate_price(7500)
