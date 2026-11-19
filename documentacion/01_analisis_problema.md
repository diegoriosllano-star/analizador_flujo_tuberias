# 01. Análisis del problema

## 1. Nombre del problema y asignatura

**Problema:** Análisis de flujo en una tubería.  
**Asignatura:** Mecánica de Fluidos.

## 2. Descripción y justificación

En Mecánica de Fluidos se estudia el comportamiento de los fluidos que circulan a través de tuberías. Para analizar un flujo es necesario conocer datos como el diámetro de la tubería, el caudal, la densidad y la viscosidad del fluido.

A partir de estos datos es posible calcular el área transversal de la tubería, la velocidad promedio del fluido y el número de Reynolds. Este último permite determinar si el régimen del flujo es laminar, de transición o turbulento.

El problema es adecuado para desarrollarse mediante una aplicación en Python porque contiene entradas, operaciones matemáticas, condiciones, validaciones y varios resultados que pueden organizarse mediante programación orientada a objetos.

## 3. Entradas

### Diámetro
- Nombre: diámetro
- Tipo de dato: float
- Unidad: metros (m)
- Restricción: debe ser mayor que cero.
- Significado: diámetro interior de la tubería.

### Caudal
- Nombre: caudal
- Tipo de dato: float
- Unidad: metros cúbicos por segundo (m**3/s)
- Restricción: debe ser mayor que cero.
- Significado: volumen de fluido que circula por unidad de tiempo.

### Densidad
- Nombre: densidad
- Tipo de dato: float
- Unidad: kilogramos por metro cúbico (kg/m**3)
- Restricción: debe ser mayor que cero.
- Significado: masa del fluido por unidad de volumen.

### Viscosidad dinámica
- Nombre: viscosidad
- Tipo de dato: float
- Unidad: pascal-segundo (Pa*s)
- Restricción: debe ser mayor que cero.
- Significado: resistencia interna del fluido al movimiento.

## 4. Procesos

La aplicación realizará los siguientes cálculos:

### Área transversal

A = πD**2 / 4

donde:

- A = área transversal de la tubería.
- D = diámetro interior de la tubería.

### Velocidad promedio

V = Q / A

donde:

- V = velocidad del fluido.
- Q = caudal.
- A = área transversal.

### Número de Reynolds

Re = (ρVD) / μ

donde:

- Re = número de Reynolds.
- ρ = densidad.
- V = velocidad.
- D = diámetro.
- μ = viscosidad dinámica.

### Clasificación del flujo

El régimen se determinará de acuerdo con el número de Reynolds:

- Re < 2300: flujo laminar.
- 2300 ≤ Re ≤ 4000: flujo de transición.
- Re > 4000: flujo turbulento.

También se validará que todos los datos ingresados sean mayores que cero.

## 5. Salidas esperadas

La aplicación mostrará:

- Área transversal de la tubería en m**2.
- Velocidad promedio del fluido en m/s.
- Número de Reynolds.
- Régimen del flujo: laminar, transición o turbulento.
- Resumen de los datos ingresados.

Además, cada análisis realizado podrá almacenarse en un historial para consultar resultados anteriores.


## 6. Ejemplo original resuelto

Como ejercicio original se utiliza un problema trabajado previamente en la asignatura de Mecánica de Fluidos.

En el ejercicio se analiza el flujo de agua a través de una tubería circular utilizando los siguientes datos:

- Diámetro interior de la tubería: 0.050 m
- Caudal: 0.002 m³/s
- Densidad del agua: 1000 kg/m³
- Viscosidad dinámica: 0.001 Pa·s

El procedimiento realizado consistió primero en calcular el área transversal de la tubería:

A = πD**2 / 4

obteniendo aproximadamente:

A = 1.9635 × 10**-3 m**2

Posteriormente se calculó la velocidad promedio del agua mediante:

V = Q / A

obteniendo aproximadamente:

V = 1.01 m/s

Después se calculó el número de Reynolds mediante:

Re = ρVD / μ

obteniendo aproximadamente:

Re = 50,930

Finalmente, al comparar el número de Reynolds con los límites de clasificación del flujo, se determinó que:

Re > 4000

por lo tanto, el régimen del flujo es turbulento.

Este ejercicio será utilizado como caso original de validación de la aplicación, comparando los resultados obtenidos manualmente con los resultados calculados por el programa.

La evidencia original se encuentra en:

`evidencias/problema_original/evidencia_original.png`

## 7. Alcance de la aplicación

La aplicación permitirá:

1. Ingresar los datos de una tubería y del fluido.
2. Validar que los datos sean mayores que cero.
3. Calcular el área transversal.
4. Calcular la velocidad promedio.
5. Calcular el número de Reynolds.
6. Clasificar el régimen del flujo.
7. Mostrar los resultados obtenidos.
8. Guardar los análisis realizados en una lista.
9. Consultar el historial de análisis.
10. Regresar al menú principal o finalizar el programa.

## 8. Cumplimiento de los requisitos técnicos

El problema cumple con los requisitos del proyecto porque:

- Fue estudiado previamente en Mecánica de Fluidos.
- Tiene entradas, procesos y salidas claramente identificables.
- Utiliza operaciones matemáticas.
- Requiere decisiones para clasificar el régimen del flujo.
- Permite validar datos de entrada.
- Puede desarrollarse mediante una aplicación de consola.
- Permite utilizar al menos dos clases con responsabilidades diferentes.
- Utiliza una lista para almacenar diferentes análisis.
- Puede implementarse mediante un menú con un ciclo.
- Permite desarrollar y documentar al menos cinco casos de prueba.
- Puede compararse con un ejercicio previamente resuelto para validar los cálculos.

