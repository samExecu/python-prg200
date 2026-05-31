#dummy data
sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]

#function to check water level
def check_water_level(location, waterLevel):

  #if water level is below 3 m -> Safe
  if waterLevel < 3:
    return "Safe"

  #if water level is between 3 m and 5 m -> Warning
  elif 3 <= waterLevel <= 5:
    return "Warning — Alert nearby villages"

  #if water level is above 5 m -> Danger
  else:
    return "DANGER — Evacuate immediately!"

#Going through each sensor reading
for location, waterLevel in sensors:
  alert = check_water_level(location, waterLevel)
  print(f"{location} ({waterLevel} m): {alert}")
