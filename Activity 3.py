import math

height = float(input("Enter the height of the cylinder: "))# Ask the user to input the height of the cylinder

pi_initial = 3.141592# Given initial value of pi

pi = round(pi_initial, 2)# Rounding it to 2 decimal places


diameter = float(input("Enter the diameter of the cylinder: "))# Ask the user to input the diameter of the cylinder's circular end


radius = diameter / 2# Calculate the radius of the cylinder's circular end



volume = pi * radius ** 2 * height# Calculate the volume of the cylinder using the formula: volume = pi * radius^2 * height


print(f"The volume of the cylinder is: {volume} cubic units.")# Output the calculated volume
