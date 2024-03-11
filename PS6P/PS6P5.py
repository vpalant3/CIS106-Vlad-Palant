user_response = input("Do you want to continue? (Enter 'Yes' to continue): ")
if user_response == "Yes":
    discount_total = 0
    while True:
        quantity = float(input("Enter the quantity of the item: "))
        price = float(input("Enter the price of the item: "))
        extended_price = quantity * price
        
        if extended_price > 10000.00:
            discount_percent = 0.25
        else:
            discount_percent = 0.10
        
        discount_amount = extended_price * discount_percent
        total = extended_price - discount_amount
        
        discount_total += discount_amount
        
        print(f"Extended price: {extended_price}")
        print(f"Discount amount: {discount_amount}")
        print(f"Total: {total}")
        
        user_response = input("Do you want to do this loop again? (Enter 'Yes' to continue): ")
        if user_response != "Yes":
            break
    
    print(f"Sum of all discounts: {discount_total}")