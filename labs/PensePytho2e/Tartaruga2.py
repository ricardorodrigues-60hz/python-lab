import turtle
import math




def circulo(t, r):
    arc(t, r, 360)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360 
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for _ in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def polyline(t, n, length, angle):
    """
    Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)




bob = turtle.Turtle()
arc(bob, r=120, angle=90)
turtle.done()