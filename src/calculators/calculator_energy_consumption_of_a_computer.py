def energy_consumption(p, h):
  return (p * h * 30)/1000

def main():
  print("Energy consumption of a computer")
  # Object: Calculate the energy consumption in kWh of a computer that operates h hours a day with power P (W), during a month of 30 days.
  # Variabkes or components: e(Energy consumption), h(hours a day), p(Power)

  # Possible errors
  try:
    h = float(input("Enter the value of hours the computer operates a day: "))
    p = float(input("Enter the value of the power of the computer (W): "))
  except ValueError:
    print("Error: Enter only numbers, not letters or symbols")
    return

  if not 0 < h <= 24:
    print("Error: Hours per day cannot exceed 24 (using 24 for calculation)")
    return
  if not 0 < p <= 2500:
    print("Error: Enter only values upper than zero")
    return
  
  # Process
  e = energy_consumption(p, h)
  
  # Results
  print(f"\nResults")
  print(f"• Daily usage: {h} hours")
  print(f"• Power consumption: {p} W")
  print(f"• Monthly consumption: {e:.2f} kWh")

if __name__ == "__main__":
  main()