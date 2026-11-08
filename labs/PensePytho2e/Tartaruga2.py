import turtle
import math


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)



bob = turtle.Turtle()

polygon(bob, 7, 70)

turtle.done()