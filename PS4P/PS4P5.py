last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: "))

adjusted_gross_income = gross_income - dependents * 12000

if adjusted_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_gross_income * tax_rate
if income_tax < 0:
    income_tax = 100

print("Last Name:", last_name)
print("Gross Income:", gross_income)
print("Number of Dependents:", dependents)
print("Adjusted Gross Income:", adjusted_gross_income)
print("Income Tax:", income_tax)