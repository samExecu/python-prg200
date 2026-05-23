#dummy data
trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

#gettings the distance and calculating the rate accordingly and returning the resulting rate
def rateCalculator(distance):
  if(distance <= 2):
    return 150
  elif (distance <= 10):
    return 150 + ((distance - 2) * 35)
  else:
    return (430 + ((distance - 10) * 28))

hours = [22, 23, 24, 1, 2, 3, 4, 5]

#interating over the list and checking if the ride is aplicable for Night Surcharge or not
for index, trip in enumerate(trips):
  print(f"Ride {index + 1}: ")
  if trip["hour"] in hours:
    print("Additional Night Surcharge of 10%")
    newTotalFare = (rateCalculator(trip["distance"])) * 1.1
    print(f"Total Fare: {newTotalFare}\n")
  else:
    print(f"Total Fare: {rateCalculator(trip["distance"])}\n")


