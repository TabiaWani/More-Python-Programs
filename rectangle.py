import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed (1 is slowest, 0 is fastest)
t.speed(0)

# Set the fill color
t.fillcolor("blue")

# Start filling
t.begin_fill()

# Draw the rectangle
t.forward(200)  # Draw the top side
t.left(90)      # Turn left by 90 degrees
t.forward(100)  # Draw the right side
t.left(90)      # Turn left by 90 degrees
t.forward(200)  # Draw the bottom side
t.left(90)      # Turn left by 90 degrees
t.forward(100)  # Draw the left side

# End filling
t.end_fill()

# Prevent the window from closing immediately
turtle.done()




#circle
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed (1 is slowest, 0 is fastest)
t.speed(1)

# Set the fill color
t.fillcolor("green")

# Start filling
t.begin_fill()

# Draw the circle
t.circle(100)  # Radius of the circle is 100

# End filling
t.end_fill()

# Prevent the window from closing immediately
turtle.done()

