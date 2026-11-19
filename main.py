from clases.tuberia import Tuberia
from clases.analisis_flujo import AnalisisFlujo


def realizar_analisis(historial):
    diametro = float(input("Diámetro de la tubería (m): "))
    caudal = float(input("Caudal (m³/s): "))
    densidad = float(input("Densidad del fluido (kg/m³): "))
    viscosidad = float(input("Viscosidad dinámica (Pa·s): "))

    if diametro <= 0 or caudal <= 0 or densidad <= 0 or viscosidad <= 0:
        print("Todos los datos deben ser mayores que cero.")
        return

    tuberia = Tuberia(diametro, caudal)
    analisis = AnalisisFlujo(tuberia, densidad, viscosidad)

    area = tuberia.calcular_area()
    velocidad = tuberia.calcular_velocidad()
    reynolds = analisis.calcular_reynolds()
    regimen = analisis.clasificar_flujo()

    print("\nRESULTADOS DEL ANÁLISIS")
    print(f"Diámetro: {diametro:.4f} m")
    print(f"Caudal: {caudal:.6f} m³/s")
    print(f"Densidad: {densidad:.2f} kg/m³")
    print(f"Viscosidad: {viscosidad:.6f} Pa·s")
    print(f"Área: {area:.7f} m²")
    print(f"Velocidad: {velocidad:.4f} m/s")
    print(f"Número de Reynolds: {reynolds:.2f}")
    print(f"Régimen del flujo: {regimen}")

    historial.append({
        "diametro": diametro,
        "caudal": caudal,
        "densidad": densidad,
        "viscosidad": viscosidad,
        "area": area,
        "velocidad": velocidad,
        "reynolds": reynolds,
        "regimen": regimen
    })


def mostrar_historial(historial):
    if len(historial) == 0:
        print("\nNo existen análisis registrados.")
        return

    print("\nHISTORIAL DE ANÁLISIS")

    for i, registro in enumerate(historial, start=1):
        print(f"\nAnálisis {i}")
        print(f"Diámetro: {registro['diametro']:.4f} m")
        print(f"Caudal: {registro['caudal']:.6f} m³/s")
        print(f"Reynolds: {registro['reynolds']:.2f}")
        print(f"Régimen: {registro['regimen']}")


def mostrar_menu():
    print("\nANALIZADOR DE FLUJO EN TUBERÍAS")
    print("1. Realizar nuevo análisis")
    print("2. Mostrar historial de análisis")
    print("0. Salir")


def main():
    historial = []
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            realizar_analisis(historial)
        elif opcion == "2":
            mostrar_historial(historial)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()