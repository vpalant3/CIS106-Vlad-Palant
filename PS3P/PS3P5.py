fixed_costs = float(input("Enter fixed costs: "))
price_per_unit = float(input("Enter price per unit: "))
cost_per_unit = float(input("Enter cost per unit: "))

break_even_point = fixed_costs / (price_per_unit - cost_per_unit)
print("Break even point:", break_even_point)