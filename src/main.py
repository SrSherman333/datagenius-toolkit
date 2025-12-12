# import modules
import sys
import os

# Find the modules in the folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "calculators"))

def menu():
  print("\n" + "="*40)
  print("        DATAGENIUS TOOLKIT")
  print("="*40)
  print("1. Temperature Conversion")
  print("2. Cloud Storage Cost")
  print("3. Execution Time Calculator")
  print("4. Euclidean Distance Calculator")
  print("5. Average Grade")
  print("6. Simple Interest Calculator")
  print("7. Average Speed of a Drone")
  print("8. Body Mass Index Calculator")
  print("9. Calculator Energy Consumption of a Computer")
  print("10. Currency Conversion")
  print("0. Leave")
  print("="*40)

def main():
# Object: Create a menu in console
# Variables or components: option (Select a option)

# Process
while True:
  menu()
  option = input("Choose an option (0-9): ")

  if option == "0": # Option 0 ---------------------
    print("See you later :>")
    break
  elif option == "1": # Option 1 -------------------
    try:
      import temperature_conversion
      temperature_conversion.main()
    except ImportError:
      print('Error: Could not load the "Temperature Conversion" module.')
      print('Please make sure "temperature_conversion.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "2": # Option 2 --------------------
    try:
      import cloud_storage_cost
      cloud_storage_cost.main()
    except ImportError:
      print('Error: Could not load the "Cloud Storage Cost" module.')
      print('Please make sure "cloud_storage_cost.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "3": # Option 3 -------------------
    try:
      import execution_time_calculator
      execution_time_calculator.main()
    except ImportError:
      print('Error: Could not load the "Execution Time Calculator" module.')
      print('Please make sure "execution_time_calculator.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "4": # Option 4 ------------------------
    try:
      import euclidean_distance_calculator
      euclidean_distance_calculator.main()
    except ImportError:
      print('Error: Could not load the "Euclidean Distance Calculator" module.')
      print('Please make sure "euclidean_distance_calculator.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "5": # Option 5 --------------
    try:
      import average_grade
      average_grade.main()
    except ImportError:
      print('Error: Could not load the "Average Grade" module.')
      print('Please make sure "average_grade.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "6": # Option 6 ------------------
    try:
      import simple_interest_calculator
      simple_interest_calculator.main()
    except ImportError:
      print('Error: Could not load the "Simple Interest Calculator" module.')
      print('Please make sure "simple_interest_calculator.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "7": # Option 7 -----------------
    try:
      import average_speed_of_a_drone
      average_speed_of_a_drone.main()
    except ImportError:
      print('Error: Could not load the "Average Speed of a Drone" module.')
      print('Please make sure "average_speed_of_a_drone.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "8": # Option 8 --------------------
    try:
      import body_mass_index_calculator
      body_mass_index_calculator.main()
    except ImportError:
      print('Error: Could not load the "Body Mass Index Calculator" module.')
      print('Please make sure "body_mass_index_calculator.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "9": # Option 9 -----------------
    try:
      import calculator_energy_consumption_of_a_computer
      calculator_energy_consumption_of_a_computer.main()
    except ImportError:
      print('Error: Could not load the "Calculator Energy Consumption of a Computer" module.')
      print('Please make sure "calculator_energy_consumption_of_a_computer.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  elif option == "10": # Option 10 -------------------
    try:
      import currency_conversion
      currency_conversion.main()
    except ImportError:
      print('Error: Could not load the "Currency COnversion" module.')
      print('Please make sure "currency_conversion.py" exists in the calculators folder.')
    except Exception as e:
      print(f"An unexpected error occurred while running the program: {e}")
  else:
    print("Error: Invalid option, try again")

if __name__ == "__main__":
  main()
