def calculate_average(n1,n2,n3,n4):
  return (n1+n2+n3+n4)/4

def main():
  print("Average grade")
  # Object: Calculate the average of 4 grades for a student
  # Variables or components: n(Average), n1(Grade 1), n2(Grade 2), 3(Grade 3), 4(Grade 4)

  # Possible errors
  try:
    n1 = float(input("Enter the value of the grade 1: "))
    n2 = float(input("Enter the value of the grade 2: "))
    n3 = float(input("Enter the value of the grade 3: "))
    n4 = float(input("Enter the value of the grade 4: "))
  except ValueError:
    print("Error: Please enter only numbers, not letters or symbols")
    return

  if n1 < 0 or n2 < 0 or n3 < 0 or n4 < 0:
    print("Error: Please enter only numbers greater than or equal to zero")
    return

  # Process
  n = calculate_average(n1,n2,n3,n4)
  
  # Results
  print(f"\nResults:")
  print(f"The average of the student is {n:.2f}")

if __name__ == "__main__":
  main()