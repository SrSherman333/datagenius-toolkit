def euclidean_distance(x1, y1, x2, y2):
  return ((x2-x1)**2 + (y2-y1)**2)**0.5

def main():
  print("Distance between two points")
  # Object: Given the coordinates (x1, y1) and (x2, y2), calculate the Euclidean distance between both points.
  # Variables or components: d(Euclidean distance), x1(Coordinate x1), y1(Coordinate y1), x2(Coordinate x2), y2(Coordinate y2)

  # Possible errors
  try:
    x1 = int(input("Enter the value of point x1: "))
    y1 = int(input("Enter the value of point y1: "))
    x2 = int(input("Enter the value of point x2: "))
    y2 = int(input("Enter the value of point y2: "))
  except ValueError:
    print("Error: Please enter only numeric and integer values")
    return
    
  # Process
  d = euclidean_distance(x1, y1, x2, y2)
  
  # Results
  print(f"\nResults")
  print(f"Coordinate 1: ({x1}, {y1})")
  print(f"Coordinate 2: ({x2}, {y2})")
  print(f"The Euclidean distance between both points is: {d:.2f}")

if __name__ == "__main__":
  main()