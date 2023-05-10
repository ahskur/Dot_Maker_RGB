# import colorgram
import random
import turtle
from turtle import *

turtle.colormode(255)

# Extract colors from picture and use as color list

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 15)
#
# for color in colors:
#      r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#      rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(16, 27, 55), (69, 94, 130), (186, 161, 120), (140, 88, 62), (138, 157, 181), (134, 75, 95), (62, 17, 9), (183, 140, 159), (128, 29, 48), (72, 107, 85), (69, 17, 27)]


# Define the brush as dot_maker
dot_maker = Turtle()
dot_maker.hideturtle()


# Debug speed
dot_maker.speed(0)

# Make so dot_maker goes to the lower end of the canvas for alignment and space
dot_maker.penup()
dot_maker.setheading(225)
dot_maker.forward(300)
dot_maker.setheading(0)


def make_dot():
    dot_maker.dot(20,random.choice(color_list))
    dot_maker.penup()
    dot_maker.forward(50)
    dot_maker.pendown()

def go_next_row():
    dot_maker.penup()
    dot_maker.setheading(90)
    dot_maker.forward(50)
    dot_maker.setheading(180)
    dot_maker.forward(500)
    dot_maker.setheading(0)


for _ in range(1,101):
    make_dot()
    if _ % 10 == 0:
        go_next_row()
    dot_maker.hideturtle()

screen = Screen()
screen.exitonclick()