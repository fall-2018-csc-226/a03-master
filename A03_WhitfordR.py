######################################################################
# Author: Rebekah Whitford
# Username: WhitfordR
# Docs link: https://docs.google.com/document/d/1BSssHhYmqR5OmFmDy31BBGwogwgCtxlDFFBjO2v4img/edit?usp=sharing

# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
######################################################################


def make_house(shape):
    """
    Makes the rectangle that makes up the house

    :return: None
    """

    shape.color("#4B0082")
    shape.begin_fill()
    for side in range(2):
        shape.forward(140)
        shape.right(90)
        shape.forward(200)
        shape.right(90)
    shape.end_fill()

def make_chimney(shape, x, y):
    """
    Adds a chimney to the house.

    :param shape: the turtle
    :param x: the x coordinate
    :param y: the y coordinate
    :return: None
    """
    shape.penup()
    shape.setpos(x, y)
    shape.pendown()
    shape.color("#4B0082")
    shape.begin_fill()
    for side in range(2):
        shape.forward(30)
        shape.right(90)
        shape.forward(20)
        shape.right(90)
    shape.end_fill()

def make_window(shape, x, y):
    """
    Adds a window to the house.

    :param shape: the turtle
    :param x: the x coordinate
    :param y: the y coordinate
    :return: None
    """
    shape.penup()
    shape.setpos(x, y)
    shape.pendown()
    shape.color('violet')
    shape.begin_fill()
    for side in range(2):
        shape.forward(30)
        shape.right(90)
        shape.forward(20)
        shape.right(90)
    shape.end_fill()

def make_door(shape):
    """
    Adds a door to the house.

    :param shape: a Turtle object
    :return: None
    """
    shape.penup()
    shape.setpos(35, -150)
    shape.pendown()
    shape.color("violet")
    shape.begin_fill()
    for side in range(2):
        shape.forward(85)
        shape.right(90)
        shape.forward(50)
        shape.right(90)
    shape.end_fill()


def make_smoke(shape):
    """
    adds smoke to the chimney
    :return:
    """
    shape.penup()
    shape.setpos(85, 30)
    shape.color("gray")
    shape.left(90)
    shape.pendown()
    shape.pensize(10)
    for side in range(7):
        shape.forward(15)
        shape.right(90)
        shape.forward(10)
        shape.left(90)


def main():
    """
    makes a house

    :return: None
    """
    import turtle               # allows use of the turtles library
    shape = turtle.Turtle()
    wn = turtle.Screen()        # Set up the window and its attributes
    wn.bgcolor("lavender")
    wn.title("lavender fields and farmhouse")

    make_house(shape)

    make_chimney(shape, 75, 20)

    make_window(shape, 35, -80)
    make_window(shape, 90, -80)
    make_window(shape, 35, -30)
    make_window(shape, 90, -30)

    make_door(shape)

    make_smoke(shape)

    wn.exitonclick()


main()                          # Calls the main function
