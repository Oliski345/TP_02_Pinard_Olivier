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

# 3
class Etudiant:
    def __init__(self, id, nom, notes=None, annee_naissance=2009):
        self.__id = id
        self.__nom = nom
        self.__notes = notes
        self.__annee_naissance = annee_naissance
        self.notes = [notes for notes in self.__notes if 0 <= notes <= 20]

    @property
    def get_nom(self):
        return self.__nom

    @get_nom.setter
    def get_nom(self, nom):
        if nom == "":
            nom = "Julia"
            self.__nom = nom

    @property
    def get_annee_naissance(self):
        return self.__annee_naissance
    @get_annee_naissance.setter
    def get_annee_naissance(self, annee_naissance):
        if not(0 <= annee_naissance <= 2025):
            annee_naissance = 2009
            self.__annee_naissance = annee_naissance
    @property
    def get_notes(self):
        return self.__notes
    @get_notes.setter
    def get_notes(self, notes):
        if 0 <= notes <= 20:
            self.__notes = notes
        else: self.__notes = 10

    def get_moyenne(self):
        if len(self.notes) == 0:
            return 0
        else:
            return sum(self.notes) / len(self.notes)
    def get_age(self):
        return 2025 - self.__annee_naissance

etu1 = Etudiant(1,"Mike",notes=[17,20, 8],annee_naissance=2006)
print(etu1.get_moyenne())
print(etu1.get_age())
etu2 = Etudiant(2, "Justin", notes=[16,2, 13,18],annee_naissance=1988)
print(etu2.get_moyenne())
print(etu2.get_age())
etu3 = Etudiant(3,"Juliette", notes=[20,3,8,12], annee_naissance=1657)
print(etu3.get_moyenne())
print(etu3.get_age())


