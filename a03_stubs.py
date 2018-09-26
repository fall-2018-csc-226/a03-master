#####################################################################
# Author: Jacob Hill
# Username: hilljac
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draws a cool picture
# google doc: https://docs.google.com/document/d/1gryHmJlAnhn5CQbHbTDOBaYJY4GSyt_H1st5oAbi1mM/edit#
######################################################################
# Acknowledgements:

#Showed me how to draw circles
#https://www.blog.pythonlibrary.org/2012/08/06/python-using-turtles-for-drawing/
#
#useful delay tool I imported
#https://www.tutorialspoint.com/python/python_date_time.htm

#Quick and easy color picking tool
#https://www.google.com/search?q=rgbcolorpicker&rlz=1C1GCEA_enUS747US758&oq=rgbcolorpicker&aqs=chrome..69i57j0l5.6726j0j7&sourceid=chrome&ie=UTF-8
######################################################################

import turtle
import time

"""
draws out "wow" as a final flourish of the animation
"""
def wow():
    pen3.pensize(4)
    pen3.speed(1)
    pen3.penup()
    pen3.forward(120)
    pen3.left(90)
    pen3.forward(200)
    pen3.right(145)

    pen3.pendown()
    pen3.forward(40)
    pen3.left(135)
    pen3.forward(35)
    pen3.right(135)
    pen3.forward(35)
    pen3.left(135)
    pen3.forward(40)
    pen3.penup()

    pen3.right(135)
    pen3.forward(40)
    pen3.pendown()
    pen3.circle(15)
    pen3.penup()
    pen3.left(90)
    pen3.forward(50)

    pen3.pendown()
    pen3.right(90)
    pen3.forward(40)
    pen3.left(135)
    pen3.forward(35)
    pen3.right(135)
    pen3.forward(35)
    pen3.left(135)
    pen3.forward(40)
    pen3.penup()







"""
Creates the geometric design in the top-left corner
"""
def shape1(pen,sz):
    for i in range(300):
        pen.forward(sz)
        pen.right(60)
        pen.forward(sz*.5)
        pen.right(20)
        sz = sz +.5
        print("wait for it...")

"""
draws the little dude's head and mouth
"""
def boiHead(x,y):
    pen2.fillcolor("#ffe48c")
    pen2.penup()
    pen2.setx(x)
    pen2.sety(y)
    pen2.pendown()
    pen2.begin_fill()
    pen2.circle(50)
    pen2.end_fill()

    pen2.fillcolor("#110d0b")

    pen2.pensize(4)
    pen2.penup()
    pen2.left(90)
    pen2.forward(20)
    pen2.pendown()
    pen2.begin_fill()
    pen2.right(90)
    pen2.forward(8)
    pen2.backward(16)
    pen2.right(45)
    pen2.forward(5.3)
    pen2.left(45)
    pen2.forward(5.3)
    pen2.left(45)
    pen2.speed(0)
    pen2.forward(5.3)
    pen2.end_fill()
    pen2.penup()

"""
draws the dude's eyes
"""
def boiEyes(x,y):
    pen2.fillcolor("#0575ff")
    pen2.setx(x)
    pen2.sety(y)
    pen2.left(45)
    pen2.forward(65)
    pen2.left(90)
    pen2.forward(20)
    pen2.pendown()
    pen2.begin_fill()
    pen2.circle(7)
    pen2.end_fill()
    pen2.penup()
    pen2.backward(40)
    pen2.pendown()
    pen2.begin_fill()
    pen2.circle(7)
    pen2.end_fill()
    pen2.penup()

"""
draws his body and limbs
"""
def boiBod():
    pen2.left(90)
    pen2.forward(65)
    pen2.fillcolor("#1c721f")
    pen2.begin_fill()
    for bod in range(2):
        pen2.right(90)
        pen2.forward(40)
        pen2.left(90)
        pen2.forward(100)
        pen2.left(180)

    pen2.end_fill()

    pen2.penup()
    pen2.forward(100)
    pen2.pendown()
    pen2.pensize(5)
    pen2.forward(50)
    pen2.backward(50)
    pen2.penup()
    pen2.right(90)
    pen2.forward(40)
    pen2.left(90)
    pen2.pendown()
    pen2.forward(50)
    pen2.penup()
    pen2.backward(120)
    pen2.right(30)
    pen2.pendown()
    pen2.forward(60)
    pen2.backward(60)
    pen2.left(120)
    pen2.penup()
    pen2.forward(40)
    pen2.right(30)
    pen2.pendown()
    pen2.forward(60)


#Declares "pens" and initial screen/bg color stuff
wn = turtle.Screen()
wn.bgcolor("#93d6ed")
pen = turtle.Turtle()
pen2 = turtle.Turtle()
pen3 = turtle.Turtle()

#gets the first pen ready to go
pen.speed(0)
pen.color("#ff3700")
pen.pensize(2)
pen.penup()
pen.setx(-200)
pen.sety(200)
pen.pendown()

#calls most functions
boiHead(140,-100)
boiEyes(140,-100)
boiBod()
shape1(pen,5)

#this is the flashing screen and "wow" ending feature
wn.bgcolor("#baffc5")
time.sleep(.4)
wn.bgcolor("#93d6ed")
time.sleep(.4)
wn.bgcolor("#baffc5")
time.sleep(.4)
wn.bgcolor("#93d6ed")
time.sleep(.4)
wn.bgcolor("#baffc5")
wow()



#program only quits when you tell it to
wn.exitonclick()







