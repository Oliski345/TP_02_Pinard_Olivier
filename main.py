# TP 02
# Olivier Pinard
# 2475333
from math import *
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
        return Vecteur3D(self.x == other.x and self.y == other.y and self.z == other.z)

    def __str__(self):
        return f'Vecteur: x = {self.x}, y = {self.y}, z = {self.z}'

    def calcul_norme(self):
        return f'Norme = {sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)}'

v1 = Vecteur3D(1, 2, 3)
v2 = Vecteur3D(2, 3, 4)
