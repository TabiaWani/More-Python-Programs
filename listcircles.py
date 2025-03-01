import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Circles with Different Colors")

# Create a turtle object
t = turtle.Turtle()
t.speed(2)  # Set the turtle's speed

# List of colors
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Draw circles with different colors
radius = 50  # Initial radius
for color in colors:
    t.fillcolor(color)  # Set the fill color
    t.begin_fill()  # Start filling
    t.circle(radius)  # Draw a circle
    t.end_fill()  # End filling

    # Move the turtle to the right for the next circle
    t.penup()
    t.forward(2 * radius + 20)  # Space between circles
    t.pendown()

# Finish
turtle.done()
