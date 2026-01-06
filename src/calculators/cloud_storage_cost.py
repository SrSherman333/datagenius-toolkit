def monthly_cost(gb, c):
  return gb*c

def annual_cost(cm):
  return 12*cm

def main():
  print("Cloud Storage Cost")
  # Object: Calculate the monthly and annual cost of a cloud storage service
  # Variables or Components: gb(Stored data), c(Unit cost), cm(Monthly cost), ca(Annual cost)

  # Possible errors
  try:
    gb = float(input("Enter stored data in GB: "))
    c = float(input("Enter cost per GB: "))
  except ValueError:
    print("Error: Please enter valid numbers only")
    return

  if gb <= 0 or c <= 0:
    print("Error: Values must be greater than zero")
    return

  # Process
  cm = monthly_cost(gb, c)
  ca = annual_cost(cm)

  #Results
  print(f"\nResults")
  print(f"The monthly cost is {cm:.2f}$")
  print(f"The annual cost is {ca:.2f}$")

if __name__ == "__main__":
  main()