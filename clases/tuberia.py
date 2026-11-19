# Implementa la clase Tuberia exactamente según
# especificaciones/especificacion_tuberia.md.
# No agregues atributos, métodos ni funcionalidades adicionales.

import math


class Tuberia:
    def __init__(self, diametro, caudal):
        self.diametro = diametro
        self.caudal = caudal

    def calcular_area(self):
        return math.pi * (self.diametro ** 2) / 4

    def calcular_velocidad(self):
        area = self.calcular_area()
        return self.caudal / area