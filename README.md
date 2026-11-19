# Analizador de Flujo en Tuberías

## Descripción

Aplicación de consola desarrollada en Python para analizar el flujo de un fluido dentro de una tubería circular.

El programa permite calcular el área transversal de la tubería, la velocidad promedio del fluido, el número de Reynolds y clasificar el régimen del flujo como laminar, de transición o turbulento.

## Asignatura original

El problema utilizado como base fue estudiado previamente en la materia de **Mecánica de Fluidos**.

## Objetivo

Desarrollar una aplicación utilizando los conceptos vistos en Programación II, incluyendo variables, operaciones, condiciones, ciclos, listas, funciones, clases, atributos, constructores, métodos y objetos.

## Funcionalidades

La aplicación permite:

- Realizar un nuevo análisis de flujo.
- Ingresar diámetro, caudal, densidad y viscosidad.
- Validar que los datos sean mayores que cero.
- Calcular el área transversal de la tubería.
- Calcular la velocidad promedio del fluido.
- Calcular el número de Reynolds.
- Clasificar el régimen del flujo.
- Guardar varios análisis en un historial.
- Consultar el historial desde el menú principal.

## Clases

### Tuberia

Representa una tubería circular.

Atributos:

- `diametro`
- `caudal`

Métodos:

- `calcular_area()`
- `calcular_velocidad()`

### AnalisisFlujo

Realiza el análisis del fluido utilizando un objeto de la clase `Tuberia`.

Atributos:

- `tuberia`
- `densidad`
- `viscosidad`

Métodos:

- `calcular_reynolds()`
- `clasificar_flujo()`

## Requisitos

- Python
- Visual Studio Code
- Git
- GitHub

No se requieren bibliotecas externas.

## Instalación

Clonar o descargar el repositorio.

Crear el entorno virtual:

`python -m venv .venv`

Activarlo en Windows:

`.venv\Scripts\activate`

## Ejecución

Ejecutar desde la carpeta principal:

`python main.py`

## Ejemplo

Datos:

- Diámetro: 0.050 m
- Caudal: 0.002 m**3/s
- Densidad: 1000 kg/m**3
- Viscosidad: 0.001 Pa*s

Resultados aproximados:

- Área: 0.0019635 m**2
- Velocidad: 1.0186 m/s
- Número de Reynolds: 50929.58
- Régimen: Turbulento

Este caso corresponde al problema original trabajado en Mecánica de Fluidos.

## Pruebas

Los casos de prueba y resultados obtenidos se encuentran documentados en:

`documentacion/02_pruebas.md`

Las capturas de ejecución se encuentran en:

`evidencias/ejecuciones/`

La evidencia del problema original se encuentra en:

`evidencias/problema_original/`