from abc import abstractmethod, abstractclassmethod, ABC
import turtle
import math


class FormaGeometrica(ABC):
    
    def __init__(self, tamanho:int, lados:int, angulo:int, x:int, y:int):
        self.tamanho = tamanho
        self.lados = lados
        self.angulo = angulo
        self.x = x
        self.y = y


    @abstractmethod
    def desenhar(self, x, y):
        """
        Toda classe que estender FormaGeometrica
        sera obrigada a implementar este método
        """

        pass

class Quadrado(FormaGeometrica):
    lados:int = 4
    angulo:int = 90

    def __init__(self, tamanho, x, y):
        
        super().__init__(tamanho=tamanho, lados=Quadrado.lados, angulo=Quadrado.angulo, x=x, y=y)


    def desenhar(self, x, y):
        
        t = turtle.Turtle()
        t.speed(3)

        for _ in range(self.lados):

            t.fd(self.tamanho)
            t.lt(self.angulo)

        turtle.done()

class Cubo(Quadrado):
    def __init__(self, tamanho, x, y):
        # Chama o construtor do Quadrado, herdando tamanho, lados e angulo
        super().__init__(tamanho, x, y)

    def teleporta(self, t, x: int, y: int):
        """Sua funcao original adaptada como metodo."""
        t.teleport(x, y)

    def tracejado_reto(self, t, angulo: int, tamanho: int):
        """Sua funcao original adaptada usando a tartaruga do parametro."""
        t.left(angulo)  # lt
        t.forward(tamanho)  # fd

    def desenhar(self, x, y):

        bob = turtle.Turtle()
        bob.speed(3)
        
        deslocamento = self.tamanho // 2 

        # 1. Desenha a primeira face na posição base da instância
        bob.teleport(self.x, self.y)
        for _ in range(self.lados):
            bob.forward(self.tamanho)
            bob.right(self.angulo)

        # 2. Desenha a segunda face deslocada
        bob.teleport(self.x + deslocamento, self.y + deslocamento)
        for _ in range(self.lados):
            bob.forward(self.tamanho)
            bob.right(self.angulo)

        # 3. Executa as suas 4 retas originais utilizando os metodos da classe
        self.teleporta(bob, x + deslocamento, y + (self.tamanho + deslocamento))
        self.tracejado_reto(bob, 225, deslocamento + 25)

        self.teleporta(bob, x + deslocamento, y + deslocamento)
        self.tracejado_reto(bob, 0, deslocamento + 25)

        self.teleporta(bob, x + (self.tamanho + deslocamento), y + deslocamento)
        self.tracejado_reto(bob, 0, deslocamento + 25)

        self.teleporta(bob, x + (self.tamanho + deslocamento), y + (self.tamanho + deslocamento))
        self.tracejado_reto(bob, 0, deslocamento + 25)

        turtle.done()

# --- Executando o codigo ---
# Instanciamos o Cubo herdando a logica de tamanho
meu_cubo = Cubo(tamanho=100, x=0, y=0)
meu_cubo.desenhar(x=0, y=0)

def circulo(t, raio: int):
    t.circle(radius=raio)


# def teleporta(t, x: int, y:int):
#     t.teleport(x, y)


# def tracejado_reto(t, angulo:int, tamanho:int):
#     bob.lt(angulo)
#     bob.fd(tamanho)

# def desenha_cubo(bob, x: int, y:int):
#     teleporta(bob, x, y)
#     quadrado(bob, 100)
#     teleporta(bob, x+50, y+50)
#     quadrado(bob, 100)
#     teleporta(bob, x+50, y+150)
#     tracejado_reto(bob, 225, +75)
#     teleporta(bob, x+50, y+50)
#     tracejado_reto(bob, 0, 75)
#     teleporta(bob, x+150, y+50)
#     tracejado_reto(bob, 0, 75)
#     teleporta(bob, x+150, y+150)
#     tracejado_reto(bob, 0, 75)


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

# bob = turtle.Turtle()
# # bob.speed(speed=100)



# polygon(bob, n=7, tamanho=70)
# circulinho_namao(bob, 30)


# # 450 x 450
# teleporta(bob, x=-450, y=-400)
# turtle.done()


