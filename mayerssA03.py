#################################################################################
# Author: Sean Mayers
# Username: mayerss
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
import random


def make_house(sean):
  """
  This function make the house next to the star
  :param sean:
  :return:
  """
  sean.penup()
  sean.backward(300)
  sean.right(90)
  sean.forward(150)
  sean.right(90)
  sean.pendown()
  for house in range(4):
      sean.forward(250)
      sean.right(90)
  sean.penup()
  sean.right(90)
  sean.forward(250)
  sean.left(40)
  sean.pendown()
  sean.forward(200)
  sean.left(102)
  sean.forward(200)
  sean.penup()
  sean.forward(100)
  sean.left(90)
  sean.forward(270)
  sean.penup()
  sean.left(126)
  sean.pendown()
  for door in range(4):
    sean.forward(100)
    sean.left(90)
def make_window(chris):
  chris.penup()
  chris.backward(500)
  chris.pendown()
  for window in range(4):
    chris.forward(40)
    chris.left(90)
  chris.penup()
  chris.forward(100)
  chris.pendown()
  for window in range(4):
    chris.forward(40)
    chris.left(90)
def make_me(yes):
  yes.penup()
  yes.forward(500)
  yes.pendown()
  for person in range(19):
    yes.forward(90)
    yes.left(70)
def make_eyes_and_body(brian):
  brian.penup()
  brian.forward(200)
  brian.left(90)
  brian.forward(100)
  brian.right(90)
  brian.forward(300)
  brian.pendown()
  for eyes in range(20):
    brian.forward(12)
    brian.left(100)
  brian.penup()
  brian.right(205)
  brian.forward(60)
  brian.pendown()
  for eye in range(20):
    brian.forward(12)
    brian.left(100)
  brian.penup()
  brian.left(45)
  brian.forward(50)
  brian.right(65)
  brian.pendown()
  brian.backward(20)
  brian.forward(80)
  brian.left(90)
  for mouth in range(5):
    brian.forward(30)
    brian.left(45)
  brian.penup()
  brian.left(120)
  brian.forward(90)
  brian.pendown()
  brian.forward(150)
  brian.left(50)
  brian.forward(50)
  brian.left(90)
  brian.penup()
  brian.forward(50)
  brian.left(130)
  brian.forward(70)
  brian.left(45)
  brian.forward(7)
  brian.pendown()
  brian.forward(50)
  brian.penup()
  brian.backward(180)
  brian.right(40)
  brian.pendown()
  brian.forward(170)
def main():
  wn = turtle.Screen()                      # makes the turtle screen
  wn.bgcolor("grey")
  sean = turtle.Turtle()
  chris = turtle.Turtle()
  brian = turtle.Turtle()
  brian.color('black')
  brian.speed(10)
  brian.pensize(5)
  yes = turtle.Turtle()
  yes.color('red')
  yes.pensize(7)
  chris.speed(10)
  yes.speed(10)
  chris.color('green')
  chris.pensize(5)
  sean.color('black')
  sean.pensize(10)
  sean.speed(15)

  colors  = ["red","light green","orange","sky blue","pink","yellow"] # list of colors to pick from
  turtle.pensize(10)
  turtle.speed(100)
  length = 5
  for count in range(115):
    color = random.choice(colors)           # Choose a random color
    turtle.forward(length)
    turtle.right(135)
    turtle.color(color)
    length = length + 5
  make_house(sean)
  make_window(chris)
  make_me(yes)
  make_eyes_and_body(brian)
  turtle.write(" I Live Next To A Star :)", font=("Arial", 16, "normal"))
  wn.exitonclick()
main()



