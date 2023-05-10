import turtle
from turtle import *
import random

# Create Harry from the blueprint (class) Turtle
harry_the_turtle = Turtle()
harry_the_turtle.shape("turtle")
harry_the_turtle.speed(15)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#          "wheat", "SlateGray", "SeaGreen"]

turtle.colormode(255)

harry_the_turtle.pensize(2)

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         harry_the_turtle.forward(100)
#         harry_the_turtle.right(angle)
#
# for shape_side_n in range(3,11):
#     harry_the_turtle.color((random.choice(colours)))
#     draw_shape(shape_side_n)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

# angle_pool = [0,90,180,270]
#
# for each_number in range(1,100):
#     harry_the_turtle.forward(random.randint(50,100))
#     if random.randint(1,1000) % 2 == 0:
#         harry_the_turtle.right(random.choice(angle_pool))
#     else:
#         harry_the_turtle.left(random.choice(angle_pool))
#     harry_the_turtle.color((random_color()))
how_tilt = 0
def draw_spirograph(angle):
    for _ in range(int(360/angle)):
        harry_the_turtle.circle(100)
        current_heading = harry_the_turtle.heading()
        harry_the_turtle.setheading(current_heading + angle)
        harry_the_turtle.color(random_color())

draw_spirograph(5)

# Create a window/screen with class Screen() and use the exitonclick() function
screen = Screen()
screen.exitonclick()