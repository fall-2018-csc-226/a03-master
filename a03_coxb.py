######################################################################
# Author: Brian Cox & Ben Christson
# Username: coxb & christsonb
#
#Google Doc: https://docs.google.com/document/d/1mzX6nEeJUVP-KF8fkC_UTUsFFCLvxnM_XIQvKY4xetM/edit?usp=sharing
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To create a house
######################################################################
# Acknowledgements:
# Used code from T03 to build the base of the house
#www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
#to get another useable color for python
#################################################################################

import turtle
b = turtle.Turtle()

def setupcanvis():
    """
    Set up the canvis
    """
    turtle.bgcolor(0.5,0,0.5)

def square():
    """
        This is to create the square
    """
    b.pencolor('red')
    b.pensize(20)
    b.pendown()
    b.forward(250)
    b.left(90)
    pass

def innersquare():
    """
        This is to create the square inside the other
    """
    b.pendown()
    b.forward(200)
    b.left(90)
    pass

def fill():
    """
    Fills the square
    """
    b.pencolor("blue")
    b.forward(210)
    b.left(90)
    b.forward(10)
    b.left(90)
    b.forward(210)
    b.right(90)
    b.forward(10)
    b.right(90)
    pass
    # ...

def firstsetup():
    """
    sets up the turtle to create the box
    """
    b.penup()
    b.left(180)
    b.forward(250)
    b.left(90)
    b.forward(250)
    b.left(90)
    pass


def fillsetup():
    """
    sets up the turtle full function
    """
    b.penup()
    b.left(90)
    b.forward(20)
    b.right(90)
    b.forward(20)
    b.pendown()

def lastlines():
    """
    #fills the last two line but doesn't  over lap the border
    """
    b.forward(210)
    b.left(90)
    b.forward(10)
    b.left(90)
    b.forward(210)
    b.left(90)

def setuproof():
    """
    To get the turtle into position to create the roof
    """
    b.penup()
    b.right(90)
    b.fd(30)
    b.right(90)
    b.fd(35)

def roof():
    """
    To create the roof of the house
    """
    b.right(30)
    b.pencolor('sandy brown')
    b.pendown()
    b.fd(270)
    b.right(120)
    b.fd(270)
    b.right(120)
    b.fd(270)

def setupwindow():
    b.penup()
    b.pencolor('white')
    b.pensize(10)
    b.left(90)
    b.fd(90)
    b.left(90)
    b.fd(60)

def rectangle():
    b.fd(40)
    b.right(90)
    b.fd(60)
    b.right(90)
    b.fd(40)
    b.right(90)
    b.fd(60)

def windowone():
    b.pendown()
    rectangle()
    b.right(90)
    b.fd(40)
    rectangle()
    b.left(90)
    b.fd(40)
    b.left(90)
    b.fd(60)
    b.left(90)
    rectangle()
    b.right(90)
    b.fd(40)
    rectangle()


# def setuprooffill():
#     """
#     Setup the turtle to fll in the roof
#     """
#     b.penup()
#     b.right(180)
#     b.fd(20)
#     b.left(45)
#     b.fd(10)
#
# def rooffill():
#     """
#     Fill the roof
#     """
#     b.pencolor()
#     b.pendown()
#     b.fd(250)
#     b.right(120)
#     b.fd(250)
#     b.right(120)
#     b.fd(250)

def main():
    """
    The main function of the program, where all things begin
    """
    window = turtle.Screen()
    setupcanvis()
    firstsetup()
    square()
    square()
    square()
    square()
    fillsetup()
    for i in range(10):
        fill()
    lastlines()
    innersquare()
    innersquare()
    innersquare()
    innersquare()
    setuproof()
    roof()
    setupwindow()
    windowone()
    window.exitonclick()

main()
