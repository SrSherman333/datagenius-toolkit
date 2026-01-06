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

        if option == "0":
            print("See you later :>")
            break
        elif option == "1":
            import temperature_conversion
            temperature_conversion.main()
        elif option == "2":
            import cloud_storage_cost
            cloud_storage_cost.main()
        elif option == "3":
            import execution_time_calculator
            execution_time_calculator.main()
        elif option == "4":
            import euclidean_distance_calculator
            euclidean_distance_calculator.main()
        elif option == "5":
            import average_grade
            average_grade.main()
        elif option == "6":
            import simple_interest_calculator
            simple_interest_calculator.main()
        elif option == "7":
            import average_speed_of_a_drone
            average_speed_of_a_drone.main()
        elif option == "8":
            import body_mass_index_calculator
            body_mass_index_calculator.main()
        elif option == "9":
            import calculator_energy_consumption_of_a_computer
            calculator_energy_consumption_of_a_computer.main()
        elif option == "10":
            import currency_conversion
            currency_conversion.main()   
        else:
            print("Error: Invalid option, try again")

if __name__ == "__main__":
    main()