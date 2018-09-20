######################################################################################################################################

# Header Block
# https://github.com/CSC236-DataStructures-F18/l02-beetle-implementation-d-s-don-t.git
# Jessie Whitaker

###########################################################################################################################################

import turtle

hot_pink = "#FFC0CB"
purple = "#70247C"
orange = "#F7B94E"


def function_house():

    h = turtle.Turtle()          # I used this function to create the basic outline of my house. In other words, I made a square.
    h.shape("turtle")

    h.color(hot_pink)
    h.setposition(0, 0)
    h.pensize(22)
    h.penup()
    h.right(90)
    h.forward(100)
    h.right(180)
    h.pendown()
    h.forward(200)
    h.right(90)
    h.forward(200)
    h.right(90)
    h.forward(200)
    h.right(90)
    h.forward(200)

    """
    Docstring for house
    """


def function_roof():

    r = turtle.Turtle()           # I used this to put a roof on the house
    r.color(hot_pink)
    r.setposition(0, 0)
    r.pensize(22)
    r.penup()
    r.left(90)
    r.forward(100)
    r.pendown()
    r.right(45)
    r.forward(145)
    r.right(90)
    r.forward(145)


def function_win():

    w = turtle.Turtle()               # I used this to create a window
    w.pencolor(hot_pink)
    w.setposition(0, 0)
    w.pensize(5)
    w.penup()
    w.forward(20)
    w.left(90)
    w.pendown()
    w.forward(22)
    w.right(90)
    w.forward(42)
    w.right(90)
    w.forward(42)
    w.right(90)
    w.forward(42)
    w.right(90)
    w.forward(21)
    w.right(90)
    w.forward(42)
    w.penup()
    w.left(90)
    w.forward(21)
    w.left(90)
    w.forward(21)
    w.left(90)
    w.pendown()
    w.forward(42)


def function_win2():

    w = turtle.Turtle()          # I used this to create a second window
    w.pencolor(hot_pink)
    w.setposition(0, 0)
    w.pensize(5)
    w.penup()
    w.forward(140)
    w.left(90)
    w.pendown()
    w.forward(22)
    w.right(90)
    w.forward(42)
    w.right(90)
    w.forward(42)
    w.right(90)
    w.forward(42)
    w.right(90)
    w.forward(21)
    w.right(90)
    w.forward(42)
    w.penup()
    w.left(90)
    w.forward(21)
    w.left(90)
    w.forward(21)
    w.left(90)
    w.pendown()
    w.forward(42)


def function_door():

    d = turtle.Turtle()          # This was used to create a small rectangle for a door, with a door knob
    d.pencolor(hot_pink)
    d.pensize(5)
    d.penup()
    d.right(90)
    d.forward(100)
    d.left(90)
    d.forward(90)
    d.left(90)
    d.pendown()
    d.forward(90)
    d.right(90)
    d.forward(30)
    d.right(90)
    d.forward(90)
    d.penup()
    d.right(180)
    d.forward(45)
    d.left(90)
    d.forward(5)
    d.pendown()
    d.circle(2)


def function_sun():

    s = turtle.Turtle()          # used this to put a sun in the sky
    s.pencolor(orange)
    s.pensize(15)
    s.penup()
    s.right(180)
    s.forward(100)
    s.right(90)
    s.forward(300)
    s.pendown()
    s.circle(80)
    s.fillcolor(orange)
    s.begin_fill()
    s.circle(80)
    s.end_fill()


def main():

    wn = turtle.Screen()                                # I used this to bring them all together for my finished house, and to add the screen
    wn.bgcolor(purple)

    function_house()
    function_roof()
    function_win()
    function_win2()
    function_door()
    function_sun()

    wn.exitonclick()


main()
