total = float(input("Enter the total for the meal: "))

tip_15 = total * 0.15
total_with_tip_15 = total + tip_15

tip_18 = total * 0.18
total_with_tip_18 = total + tip_18

tip_20 = total * 0.20
total_with_tip_20 = total + tip_20

print("With 15% Tip:")
print(f"Total:                {total}")
print(f"Tip:                     {tip_15}")
print(f"Total with Tip    {total_with_tip_15}")

print()

print("With 18% Tip:")
print(f"Total:                {total}")
print(f"Tip:                     {tip_18}")
print(f"Total with Tip    {total_with_tip_18}")

print()

print("With 20% Tip:")
print(f"Total:                {total}")
print(f"Tip:                     {tip_20}")
print(f"Total with Tip    {total_with_tip_20}")