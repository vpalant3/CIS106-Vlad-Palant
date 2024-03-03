principle = float(input("Enter principle amount of CD: $"))
years = int(input("Enter years to maturity of CD: "))

if principle > 100000:
    interest_rate = 0.06
elif 50000 <= principle <= 100000:
    if years == 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.04
else:
    interest_rate = 0.02

first_year_interest = principle * interest_rate

print(f"Principle: ${principle}")
print(f"Interest Rate: {interest_rate * 100}%")
print(f"Interest Amount for first year: ${first_year_interest}")