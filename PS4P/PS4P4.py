name = input("Enter the name of the appliance: ")
cost = float(input("Enter the cost of the appliance: "))

if cost > 1000:
    warranty_cost = cost * 0.10
else:
    warranty_cost = cost * 0.05

total_cost = cost + warranty_cost

print(f"Name of appliance: {name}")
print(f"Cost of appliance: ${cost}")
print(f"Cost of warranty: ${warranty_cost}")
print(f"Total cost (appliance + warranty): ${total_cost}")