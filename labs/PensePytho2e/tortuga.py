import turtle
import math

def quadrado(t, tamanho):
    for i in range(4):
        t.fd(tamanho)
        t.lt(90)


def circulo(t, raio: int):
    t.circle(radius=raio)


def teleporta(t, x: int, y:int):
    t.teleport(x, y)


def tracejado_reto(t, angulo:int, tamanho:int):
    bob.lt(angulo)
    bob.fd(tamanho)

def desenha_cubo(bob, x: int, y:int):
    teleporta(bob, x, y)
    quadrado(bob, 100)
    teleporta(bob, x+50, y+50)
    quadrado(bob, 100)
    teleporta(bob, x+50, y+150)
    tracejado_reto(bob, 225, +75)
    teleporta(bob, x+50, y+50)
    tracejado_reto(bob, 0, 75)
    teleporta(bob, x+150, y+50)
    tracejado_reto(bob, 0, 75)
    teleporta(bob, x+150, y+150)
    tracejado_reto(bob, 0, 75)


def polygon(t, n:int, tamanho):
    angle = 360 / n
    for i in range(n):
        t.fd(tamanho)
        t.lt(angle)

def circulinho_namao(t, raio:int):
    circumference = 2 * math.pi * raio
    n = 50
    length = circumference / n
    polygon(t, n, length)
    ...

bob = turtle.Turtle()
# bob.speed(speed=100)



polygon(bob, n=7, tamanho=70)
circulinho_namao(bob, 30)


# 450 x 450
teleporta(bob, x=-450, y=-400)
turtle.done()


