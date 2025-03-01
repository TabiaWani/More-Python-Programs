import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flower Spiral")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the fastest speed
turtle.colormode(255)  # Enable RGB color mode

# Draw a flower spiral
for i in range(360):
    t.pencolor((i % 255, (i * 2) % 255, (i * 3) % 255))  # Dynamic RGB colors
    t.circle(100)  # Draw a circle with radius 100
    t.right(10)  # Rotate the turtle slightly for the next circle

# Finish
turtle.done()
