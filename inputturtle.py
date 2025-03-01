import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Ask for first name and last name using textinput()
first_name = screen.textinput("Name Input", "Enter your first name:")
last_name = screen.textinput("Name Input", "Enter your last name:")

# Create a turtle for writing text
name_turtle = turtle.Turtle()
name_turtle.hideturtle()  # Hide the turtle cursor
name_turtle.penup()  # Lift the pen to avoid drawing lines

# Write the full name in the turtle graphics window
name_turtle.goto(0, 0)  # Set the starting position for the text
name_turtle.write(f"Your full name is: {first_name} {last_name}", align="center", font=("Arial", 16, "normal"))

# Exit on click
screen.exitonclick()