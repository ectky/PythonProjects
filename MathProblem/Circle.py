import turtle
import time


def set_to_startpos():
    myTurtle.penup()
    myTurtle.home()
    myTurtle.setpos(0, -150)
    myTurtle.pendown()


def move_half(n, side_length):
    myTurtle.forward(side_length/2)
    myTurtle.left(360/n)


def draw_polygon(n, side_length):
    for i in range(n):
        myTurtle.forward(side_length)
        myTurtle.left(360/n)

turtle.screensize()
turtle.setup(0.99, 0.9, 0, 0)
turtle.title("Hexagons to circle")

myTurtle = turtle.Turtle(shape='turtle')
myTurtle.color("magenta3")

myTurtle.speed(1)
turtle.bgcolor("ivory")

set_to_startpos()

myTurtle.pensize(3)

# myTurtle.begin_fill()
side_length = 232
move_half(6, side_length)
draw_polygon(6, side_length)
# myTurtle.end_fill()

set_to_startpos()

# myTurtle.color("black")
# myTurtle.circle(200)

myTurtle.penup()
myTurtle.left(90)
myTurtle.forward(25.7)
myTurtle.right(90)
myTurtle.pendown()

myTurtle.color("magenta3")
# myTurtle.begin_fill()
side_length = 200
move_half(6, side_length)
draw_polygon(6, side_length)
# myTurtle.end_fill()

set_to_startpos()
myTurtle.color("red")

side_length = 107.5
move_half(12, side_length)
draw_polygon(12, side_length)

set_to_startpos()
myTurtle.color("orange")
myTurtle.left(15)

side_length = 103.5
draw_polygon(12, side_length)

set_to_startpos()

myTurtle.color("green")
side_length = 53
move_half(24, side_length)
draw_polygon(24, side_length)

set_to_startpos()
myTurtle.color("blue")
myTurtle.left(7)

side_length = 52.5
draw_polygon(24, side_length)

set_to_startpos()

myTurtle.color("black")
myTurtle.pensize(6.5)
myTurtle.circle(200)

time.sleep(1000)
