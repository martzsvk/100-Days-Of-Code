from turtle import Turtle,Screen
import turtle
import random

# import colorgram
#
# colors = colorgram.extract("image.jpg", 20)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r,g,b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)

color_list = [(29, 101, 154), (181, 63, 28), (249, 168, 83), (186, 45, 111), (218, 211, 62), (242, 210, 215), (243, 154, 185), (122, 205, 188), (146, 196, 3), (175, 120, 155), (170, 204, 191), (4, 127, 70), (252, 95, 6), (236, 243, 249), (253, 196, 0), (205, 16, 94), (2, 121, 66), (169, 104, 140)]

x_position = -250
y_position = -200

martan = Turtle()
martan.speed("fastest")
martan.shape("turtle")
turtle.colormode(255)
martan.teleport(x_position, y_position)

for _ in range(10):
    for _ in range(10):
        martan.dot(20, random.choice(color_list))
        martan.penup()
        martan.forward(50)
    martan.teleport(x_position, y_position + 50)
    y_position += 50

martan.hideturtle()


screen = Screen()
screen.exitonclick()



