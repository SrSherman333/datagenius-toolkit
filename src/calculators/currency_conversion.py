def calculate_usd(m, t_usd):
  return m*t_usd

def calculate_eur(m, t_eur):
  return m*t_eur

def main():
  print("Currency conversion")
  # Object: Calculate the value in dollars and euros of an amount in local currency, using the exchange rates provided.
  # Variables or components: usd(Value in dollars), eur(Value in euros), m(Local currency), tusd(Exchange rate usd), teur(Exchange rate eur)

  # Possible errors
  try:
    m = float(input("Enter amount in local currency:"))
    t_usd = float(input("Enter USD rate (USD per 1 local unit, e.g., 0.05): "))
    t_eur = float(input("Enter EUR rate (EUR per 1 local unit, e.g., 0.045): "))
  except ValueError:
    print("Error: Enter only numbers, not letters or symbols")
    return

  if m <= 0 or t_usd <= 0 or t_eur <= 0:
    print("Error: All values must be greater than zero")
    return

  if t_usd > 10 or t_eur > 10:
    print("Warning: Exchange rates seem unusually high (> 10)")
    print("Remember: Rate should be USD/EUR per 1 local unit")
    return
  
  # Process
  usd = calculate_usd(m, t_usd)
  eur = calculate_eur(m, t_eur)
  
  # Results
  print(f"\nResults:")
  print(f"Your local amount is {m:.2f}")
  print(f"The value in dollars is {usd:.2f}$")
  print(f"The value in euros is {eur:.2f}€")

  # Additional information
  print(f"\nSummary:")
  print(f"1 local unit = ${t_usd:.4f} USD")
  print(f"1 local unit = €{t_eur:.4f} EUR")


if __name__ == "__main__":
  main()