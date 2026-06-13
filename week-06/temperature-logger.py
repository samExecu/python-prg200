import math

# Global variable
station_name = "Kathmandu Weather Station"

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]

def get_average(temps):
    # Returns the mean or the average temperature.
    return sum(temps) / len(temps)


def get_deviation(temps):
    # Returns the standard deviation
    # 'mean' = local variable
    mean = get_average(temps)

    # Calculating the variance
    variance = sum((x - mean) ** 2 for x in temps) / len(temps)

    # Calculates the standard deviation and returns it
    return math.sqrt(variance)


def get_summary(temps):
    # Displays min, max, average, and the deviation
    print(f"Station: {station_name}")
    print(f"Minimum Temperature: {min(temps)}°C")
    print(f"Maximum Temperature: {max(temps)}°C")
    print(f"Average Temperature: {get_average(temps):.2f}°C")
    print(f"Standard Deviation: {get_deviation(temps):.2f}°C")

get_summary(temperatures)

# Displaying NameError when accessing local variable outside function
print("\n--- Trying to access the local variable 'mean' outside the get_deviation()function ---")
try:
    print(mean)
except NameError as e:
    print(f"NameError: {e}")
    print("Because, 'mean' is a local variable which was defined inside the get_deviation() function, so we get an error when we try to accese it outside the function.")
