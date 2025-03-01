import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Colored Circle")

# Create a turtle object
t = turtle.Turtle()
t.speed(1)  # Set the turtle's speed

# Set the fill color
t.fillcolor("blue")  # Choose your color here
t.begin_fill()  # Start filling the shape

# Draw a circle
t.circle(100)  # Radius of the circle is 100 units

t.end_fill()  # End filling the shape

# Finish
turtle.done()
