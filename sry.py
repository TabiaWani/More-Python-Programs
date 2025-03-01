import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("SORRY")

# Create a turtle
pen = turtle.Turtle()
pen.color("blue")
pen.pensize(7)
pen.speed(3)

# Position the turtle
pen.penup()
pen.goto(-650, 0)  # Adjust the position as needed
pen.pendown()

# Write "SORRY"
pen.hideturtle()
pen.write("SORRY MAI NE TUMKO GUSSA DILAYA", font=("Arial", 50, "bold" ,"italic"), align="left")

# Keep the screen open
screen.mainloop()
