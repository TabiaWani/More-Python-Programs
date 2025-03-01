import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the fastest speed
turtle.colormode(255)  # Allows RGB color values

# Draw a colorful spiral
for i in range(360):
    t.pencolor((i % 255, (i * 2) % 255, (i * 3) % 255))  # RGB colors
    t.width(i // 100 + 1)  # Adjust the pen width
    t.forward(i * 2)  # Move forward
    t.right(59)  # Adjust the angle for a unique spiral pattern

# Finish
turtle.done()
