def speed_kmh(d,t):
  if t == 0:
    raise ValueError("Time cannot be zero")
  else:
    return d/t

def speed_ms(vkm):
  return vkm/3.6

def main():
  print("Average Speed of a Drone Calculator")
  # Object: Given the distance traveled and the time taken, calculate the average speed of the drone in km/h and m/s
  # Variables or components: vkm(Average speed in km/h), vms(Average speed in ms), d(Distance traveled), t(time taken)

  #Possible errors
  try:
    d = float(input("Enter the distance traveled (km): "))
    t = float(input("Enter the time taken (hours): "))
  except ValueError:
    print("Error: Please enter only numbers")
    return

  if d <= 0 or t <= 0:
    print("Error: Values must be greater than zero")
    return
    
  # Process
  vkm = speed_kmh(d,t)
  vms = speed_ms(vkm)
  
  # Results
  print(f"\nResults:")
  print(f"Average speed in km/h: {vkm:.2f}")
  print(f"Average speed in m/s: {vms:.2f}")

if __name__ == "__main__":
  main()