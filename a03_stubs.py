###########################################################################################
# sick nasty header block
# Thomas Guthrie is did this
# thank. Here code for shapes.
###########################################################################################
import turtle
from time import sleep


#def func_setup():
#    """
#    this what do
#    :return:
#    """
#    wn = turtle.Screen()
#    wn.bgcolor(0, 0, 0)
#    bob = turtle.Turtle()
#    bob.color("white")
#    bob.pensize(3)
#    bob.penup()
#    bob.setpos(-80, 0)
#    return bob
#    pass
    # into the ass


def func_doit(tName, w, h):
    """
    make house
    tname, width, height
    :return:
    """

    tName.pendown()
    tName.begin_fill()
    for i in range(2):   # square builder 9000
        tName.fd(w)
        tName.left(90)
        tName.fd(h)
        tName.left(90)
    tName.end_fill()
    tName.fd(w*.5)    # tREEANGLE
    tName.left(90)
    tName.fd(h)
    tName.right(90)
    tName.begin_fill()
    tName.fd(.75*w)
    tName.left(135)
    tName.fd(1.05*w)
    tName.left(90)
    tName.fd(1.05*w)
    tName.left(135)
    tName.fd(.75*w)
    tName.end_fill()
    tName.penup()
    pass
    # into the ass


def func_doall(tName,a,rnd,flps):
    """
    this what do
    tName,a,howmuchitspinny,flippies
    :return:
    """
    tName.pendown()
    for i in range(flps):
        for i in range(rnd):
            tName.backward(2)
            tName.left(a)
        if flps > 0:
            for i in range(rnd):
                tName.fd(2)
                tName.left(a)
            flps = flps - 1
        else:
            pass
    tName.penup()
    # into the ass


def main():
    """
    this what do
    :return:
    """
    wn = turtle.Screen()
    wn.bgcolor(0, 0, 0)
    bob = turtle.Turtle()
    bob.speed(0)
    bob.color("white")
    bob.pensize(3)
    bob.penup()
    bob.setpos(-80, 0)
    func_doit(bob, 20, 10)
    bob.setpos(10, 0)
    func_doall(bob, 5, 77, 19,)
    bob.setpos(100, 50)
    func_doall(bob, 4, 75, 3)
    bob.setpos(-80, -90)
    func_doall(bob, 6, 20, 14)
    bob.setpos(30, -70)
    func_doall(bob, -32, 15, 24)
    bob.setpos(150, 150)
    sleep(5)
    pass
    # into the ass


main()

