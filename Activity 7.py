import turtle

# Define variables for the pattern's structure
iterations = 12  # Number of hexagons to draw
angle_of_rotation = 30  # Angle to turn after drawing a hexagon
size_of_shape = 130  # Length of each side of the hexagon
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']  # Color options

# Set up the Turtle screen and turtle
screen = turtle.Screen()
pattern_turtle = turtle.Turtle()
pattern_turtle.speed('fastest')  # Increase drawing speed

# Function to draw a hexagon
def draw_hexagon(size):
    for _ in range(6):
        pattern_turtle.forward(size)
        pattern_turtle.right(60)

# Main loop to draw the pattern
for i in range(iterations):
    # Manually change the color by cycling through the colors list
    color = colors[i % len(colors)]  # Cycle through colors
    pattern_turtle.pencolor(color)
    
    # Draw the geometric shape (hexagon in this case)
    draw_hexagon(size_of_shape)
    
    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(angle_of_rotation)

# Hide the turtle and complete the program
pattern_turtle.hideturtle()
turtle.done()
