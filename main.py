# TP 02
# Olivier Pinard
# 2475333
from math import *
from abc import ABC, abstractmethod
# 3
class Vecteur3D:
    def __init__(self, x=1, y=1 , z=1):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vecteur3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vecteur3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalaire=2):
        return Vecteur3D(self.x * scalaire, self.y * scalaire, self.z * scalaire)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __str__(self):
        return f'Vecteur: x = {self.x}, y = {self.y}, z = {self.z}'

    def calcul_norme(self):
        return f'Norme = {sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2):.2f}'

v1 = Vecteur3D(1, 2, 3)
v2 = Vecteur3D(2, 3, 4)
v3 = (v1 + v2)
print(v3)
v4 = (v1 - v2)
print(v4)
v5 = (v1 * 4)
print(v5)
print(v1.calcul_norme())
print(v2.calcul_norme())
print(v1 == v2)

# 2
class FonctionMathématique(ABC):
    @abstractmethod
    def evaluer(self, x):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Parabole(FonctionMathématique):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluer(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def __str__(self):
        return f'fonction de la Parabole: {self.a}x**2 + {self.b}x + {self.c}'

class Exponentielle(FonctionMathématique):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def evaluer(self, x):
        return self.a * exp(self.b * x)

    def __str__(self):
        return f"fonction de l'Exponentielle: {self.a}x**{self.b}"

class Sinusoide(FonctionMathématique):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def evaluer(self, x):
        return self.a * sin(self.b * x + self.c)

    def __str__(self):
        return f"Fonction du Sinus: {self.a} * sin({self.b}x + {self.c})"
p1 = Parabole(1, 2, 3)
print(p1)
print(p1.evaluer(2))
p2 = Parabole(10, 6, 8)
print(p2)
print(p2.evaluer(50))
e1 = Exponentielle(1, 2)
print(e1)
print(e1.evaluer(2))
e2 = Exponentielle(9, 7)
print(e2)
print(e2.evaluer(5))
s1 = Sinusoide(1, 2, 3)
print(s1)
print(s1.evaluer(2))
s2 = Sinusoide(21, 34, 8)
print(s2)
print(s2.evaluer(5))
