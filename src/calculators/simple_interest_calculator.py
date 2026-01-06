def calculate_total_amount(c,i,t):
  return c*(1+i*t)

def rate_percentage(i):
  return i * (1/100)

def main():
  print("Simple Interest Calculator")
  # Object: Calculate the total amount to be paid on a simple interest loan from the initial capital, the rate and the time in years
  # Variables or components: m(Total amount), c(Initial capital), i(Rate), t(Time in years)

  # Possible errors
  try:
    c = float(input("Enter the initial capital: "))
    i = float(input("Enter the annual interest rate (%): "))
    t = float(input("Enter the time in years: "))
  except ValueError:
    print("Error: Please enter ony numbers, not letters or symbols")
    return

  if c <= 0 or i <= 0 or t <= 0:
    print("Error: All values must be greater than zero")
    return
    
  # Process
  i = rate_percentage(i)
  m = calculate_total_amount(c,i,t)
  interest = m-c
  
  # Results
  print(f"\nResults:")
  print(f"The interest earned is {interest:.2f}")
  print(f"The total amount to be paid is {m:.2f}")

if __name__ == "__main__":
  main()