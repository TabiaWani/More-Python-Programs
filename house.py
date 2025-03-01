import turtle

# Create a turtle object named 'builder'
builder = turtle.Turtle()

# Set turtle speed
builder.speed(3)
builder.pensize(3)
builder.color("black")
builder.fillcolor("lightblue")


# Draw the base of the house (rectangle)
builder.fillcolor("blue")
builder.begin_fill()
builder.forward(200)  # Width of the house
builder.left(90)
builder.forward(150)  # Height of the house
builder.left(90)
builder.forward(200)  # Width of the house
builder.left(90)
builder.forward(150)  # Height of the house
builder.left(90)
builder.end_fill()

# Draw the roof (triangle)
builder.fillcolor("red")
builder.begin_fill()
builder.goto(0, 150)      # Starting point of the roof
builder.goto(100, 250)    # Peak of the roof
builder.goto(200, 150)    # End of the roof
builder.goto(0, 150)      # Back to the starting point of the roof
builder.end_fill()

# Draw the door (rectangle)
builder.penup()
builder.goto(75, 0)
builder.pendown()
builder.fillcolor("brown")
builder.begin_fill()
builder.setheading(90)
builder.forward(75)  # Door height
builder.right(90)
builder.forward(50)  # Door width
builder.right(90)
builder.forward(75)  # Door height
builder.right(90)
builder.forward(50)  # Door width
builder.end_fill()

# Draw the left window (square)
builder.penup()
builder.goto(75, 140)
builder.pendown()
builder.fillcolor("yellow")
builder.begin_fill()
builder.forward(50)  # Bottom side
builder.left(90)
builder.forward(50)  # Right side
builder.left(90)
builder.forward(50)  # Top side
builder.left(90)
builder.forward(50)  # Left side
builder.end_fill()

# Draw the right window (square)
builder.penup()
builder.goto(165, 90)
builder.pendown()
builder.fillcolor("yellow")
builder.begin_fill()
builder.forward(50)  # Bottom side
builder.left(90)
builder.forward(50)  # Right side
builder.left(90)
builder.forward(50)  # Top side
builder.left(90)
builder.forward(50)  # Left side
builder.end_fill()


# Prevent the window from closing immediately
builder.penup()
builder.hideturtle()
turtle.done()
