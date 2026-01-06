def celsius_to_fahrenheit(c):
  return (9/5)*c+32

def celsius_to_kelvin(c):
  return c+273.15

def main(): 
  print("Temperature Conversion")
  # Object: Calculate the temperature in Fahrenheit and Kelvin from a given value in Celsius.
  # Varibles or Components: c(Celsius), f(Fahrenheit), k(Kelvin)
  
  # Possible errors
  try:
    c = float(input("Enter temperature in Celsius: "))
  except ValueError:
    print("Error: Please enter only numbers, not letters or symbols")
    return

  if c < -273.15:
    print("Error: Temperature cannot be below absolute zero (-273.15°C)")
    return

  # Calculations
  f = celsius_to_fahrenheit(c)
  k = celsius_to_kelvin(c)

  # Results
  print(f"\nResults:")
  print(f"The temperature in Fahrenheit is {f:.2f}°F")
  print(f"The temperature in Kelvin is {k:.2f}K")

if __name__ == "__main__":
  main()