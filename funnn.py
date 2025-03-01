import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.color("green")
pen.pensize(3)
pen.speed(1)

# Draw a heart shape
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# End drawing
pen.hideturtle()
turtle.done()
