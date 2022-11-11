import random
from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [
    (246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247), (197, 165, 117),
    (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22),
    (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76),
    (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89),
    (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)
]


turtle.up()
turtle.speed(0)
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

def go_and_dots():
    for _ in range(10):
      turtle.dot(20, random.choice(color_list))
      turtle.forward(50)


def next_line():
    turtle.lt(90)
    turtle.forward(50)
    turtle.lt(90)
    turtle.forward(500)


def face_east():
    turtle.st()
    turtle.rt(90)
    turtle.rt(90)


for _ in range(10):
    turtle.ht()
    go_and_dots()
    next_line()
    face_east()
turtle.ht()
screen.exitonclick()
