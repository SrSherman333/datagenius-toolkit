def time_seconds(n, v):
  if v == 0:
    raise ValueError("Velocity cannot be zero")
  else:
    return n/v

def time_minutes(ts):
  return ts/60

def main():
  print("Program Execution Time Calculator")
  # Object: Calculate execution time given operations and processing speed
  # Variables or Componentes: ts(time in seconds), tm(time in minutes), n(number of operation), v(Execution speed)

  #Possible errors
  try:
    n = int(input("Enter the number of operations: "))
    v = float(input("Enter execution speed (operations/second): "))
  except ValueError:
    print("Error: Please enter valid numbers only")
    return

  if n <= 0 or v <= 0:
    print("Error: Values must be greater than zero")
    return
  
  # Process
  ts = time_seconds(n, v)
  tm = time_minutes(ts)
  
  #Results
  print(f"\nResults:")
  print(f"Time in seconds: {ts:.2f}s")
  print(f"Time in minutes: {tm:.2f}min")

if __name__ == "__main__":
  main()