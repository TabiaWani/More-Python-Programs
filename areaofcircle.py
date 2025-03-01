import math

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius**2

# Input the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the area
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")
