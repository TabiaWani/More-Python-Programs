# Ask the user for their age
age = int(input("Enter your age: "))

# Check if the user is a child, teenager, or adult using if-elif
if age < 13:
    print("You are a child.")
elif age <= 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
    
    
    #turtle module
    
    import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Optional: Set the background color of the screen

# Create a turtle object
t = turtle.Turtle()

# Ask the user for their age
age = int(input("Enter your age: "))

# Display the message based on the age
t.penup()
t.goto(-150, 0)  # Position the turtle at a starting point
t.pendown()

if age < 13:
    t.write("You are a child.", font=("Arial", 16, "normal"))
elif 13 <= age <= 17:
    t.write("You are a teenager.", font=("Arial", 16, "normal"))
else:
    t.write("You are an adult.", font=("Arial", 16, "normal"))

# Hide the turtle after writing
t.hideturtle()

# Hold the screen until clicked
screen.exitonclick()

