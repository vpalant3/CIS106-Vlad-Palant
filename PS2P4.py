def calculate_discount(msrp, discount_percent):
  amount_off = msrp * discount_percent
  discounted_price = msrp - amount_off
  return amount_off, discounted_price

def main():

  make = input("Enter the make of the auto: ")
  model = input("Enter the model of the auto: ")
  msrp = float(input("Enter the MSRP amount: $"))
  discount_percent = float(input("Enter the discount percent (as a decimal): "))


  amount_off, discounted_price = calculate_discount(msrp, discount_percent)


  print("\nAuto Information:")
  print(f"Make: {make}")
  print(f"Model: {model}")
  print(f"MSRP: ${msrp:.2f}")
  print(f"Discount Percent: {discount_percent:.2%}")
  print(f"Amount Off: ${amount_off:.2f}")
  print(f"Discounted Price: ${discounted_price:.2f}")

if __name__ == "__main__":
  main()