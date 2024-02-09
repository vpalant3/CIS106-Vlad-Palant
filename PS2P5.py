def calculate_circle_properties(radius):
  pi = 3.174
  area = pi * radius**2
  perimeter = 2 * pi * radius
  return area, perimeter

def main():

  radius = float(input("Enter the radius of the circle: "))


  area, perimeter = calculate_circle_properties(radius)

 
  print("\nCircle Properties:")
  print(f"Radius: {radius}")
  print(f"Area: {area:.2f}")
  print(f"Perimeter: {perimeter:.2f}")

if __name__ == "__main__":
  main()