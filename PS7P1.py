principle = float(input("Enter principle amount: "))
interest_rate = float(input("Enter interest rate: "))
total_interest = 0

print("\nYear    Beginning Balance    Ending Balance")
for year in range(1, 6):
    if year == 1:
        beginning_balance = principle
    else:
        beginning_balance = ending_balance
    
    annual_interest = beginning_balance * interest_rate
    ending_balance = beginning_balance + annual_interest
    total_interest += annual_interest
    
    print(f"{year}\t${beginning_balance:.2f}\t\t${ending_balance:.2f}")

print(f"\nTotal interest earned: ${total_interest:.2f}")