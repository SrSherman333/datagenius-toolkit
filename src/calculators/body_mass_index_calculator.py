def calculate_imc(p,h):
  if h == 0:
    raise ValueError("The height cannot be zero")
  else:
    return p / h**2

def results_imc(l, imc):
  if imc < 18.5:
    return l[0]
  elif 18.5 <= imc <= 24.9:
    return l[1]
  elif 25.0 <= imc <= 29.9:
    return l[2]
  else:
    return l[3]

def main():
  print("Body Mass Index(IMC) Calculator")
  # Object: Calculate a person's body mass index (BMI) from their weight (kg) and height (m).
  # Variables or components: imc(Body mass index), p(Weight), h(Height), l(List of results)
  # World records for validation:
  # Maximum weight recorded: ~635 kg (Jon Brower Minnoch)
  # Maximum height recorded: ~2.72 m (Robert Wadlow)

  # Declarations
  l = ["Underweight",  "Normal Weight", "Weight above normal", "Obesity"]

  # Possible errors
  try:
    p = float(input("Enter the weight in kilograms(kg): "))
    h = float(input("Enter the height in meters(m): "))
  except ValueError:
    print("Error: Enter only numbers, not letter or symbols")
    return

  if not 15 <= p <= 635:
    print("Error: Weight must be between 15 and 635 kg")
    return
  if not 0.5 <= h <= 2.72:
    print("Height must be between 0.5 and 2.72 m")
    return
  
  # Process
  imc = calculate_imc(p, h)
  results = results_imc(l, imc)
  
  # Results
  print(f"\nResults")
  print(f"The Body Mass Index (IMC) is {imc:.2f}, which means you are in the category: {results}")
  print(f"\nIMC Table:")
  print(f"- Underweight: < 18.5")
  print(f"- Normal weight: 18.5 - 24.9")
  print(f"- Overweight: 25.0 - 29.9")
  print(f"- Obesity: ≥ 30.0")

if __name__ == "__main__":
  main()