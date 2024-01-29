# Conversion constant from kilometers to miles
CONVERSION_FACTOR = 0.621371

# Get user input for the distance in kilometers
kilometers = float(input("Enter the distance in kilometers: "))

# Convert the distance to miles
miles = kilometers * CONVERSION_FACTOR

# Print the result rounded to 2 decimal places
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
