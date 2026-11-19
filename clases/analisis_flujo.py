# Implementa la clase AnalisisFlujo exactamente según
# especificaciones/especificacion_analisis_flujo.md.
# No agregues atributos, métodos ni funcionalidades adicionales.

class AnalisisFlujo:
    def __init__(self, tuberia, densidad, viscosidad):
        self.tuberia = tuberia
        self.densidad = densidad
        self.viscosidad = viscosidad

    def calcular_reynolds(self):
        velocidad = self.tuberia.calcular_velocidad()
        diametro = self.tuberia.diametro

        return (self.densidad * velocidad * diametro) / self.viscosidad

    def clasificar_flujo(self):
        reynolds = self.calcular_reynolds()

        if reynolds < 2300:
            return "Laminar"
        elif reynolds <= 4000:
            return "Transición"
        else:
            return "Turbulento"