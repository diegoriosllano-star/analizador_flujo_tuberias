# Especificación de la clase AnalisisFlujo

## 1. Nombre de la clase

`AnalisisFlujo`

## 2. Objetivo y responsabilidad

Analizar el comportamiento del fluido que circula por una tubería.

La clase será responsable de calcular el número de Reynolds y determinar si el régimen del flujo es laminar, de transición o turbulento.

Utilizará un objeto de la clase `Tuberia` para obtener el diámetro y la velocidad necesarios para realizar los cálculos.

## 3. Atributos

### tuberia
- Tipo: objeto `Tuberia`
- Significado: tubería sobre la cual se realizará el análisis.

### densidad
- Tipo: `float`
- Unidad: kg/m**3
- Significado: densidad del fluido.
- Restricción: debe ser mayor que cero.

### viscosidad
- Tipo: `float`
- Unidad: Pa*s
- Significado: viscosidad dinámica del fluido.
- Restricción: debe ser mayor que cero.

## 4. Constructor

### `__init__(self, tuberia, densidad, viscosidad)`

Recibe:

- `tuberia`
- `densidad`
- `viscosidad`

Debe guardar los valores en:

- `self.tuberia`
- `self.densidad`
- `self.viscosidad`

No debe realizar cálculos dentro del constructor.

## 5. Métodos

### `calcular_reynolds(self)`

#### Objetivo

Calcular el número de Reynolds correspondiente al flujo.

#### Atributos utilizados

- `self.tuberia`
- `self.densidad`
- `self.viscosidad`

#### Algoritmo

1. Obtener la velocidad mediante:

`self.tuberia.calcular_velocidad()`

2. Obtener el diámetro mediante:

`self.tuberia.diametro`

3. Calcular el número de Reynolds utilizando:

Re = (ρVD) / μ

donde:

- Re = número de Reynolds.
- ρ = densidad del fluido.
- V = velocidad promedio.
- D = diámetro interior de la tubería.
- μ = viscosidad dinámica.

#### Resultado

Debe devolver un valor `float` correspondiente al número de Reynolds.

No debe imprimir el resultado.


### `clasificar_flujo(self)`

#### Objetivo

Determinar el régimen del flujo de acuerdo con el número de Reynolds.

#### Algoritmo

1. Obtener el número de Reynolds utilizando `calcular_reynolds()`.

2. Aplicar las siguientes condiciones:

- Si Re < 2300:
  - devolver `"Laminar"`

- Si Re está entre 2300 y 4000, incluyendo ambos límites:
  - devolver `"Transición"`

- Si Re > 4000:
  - devolver `"Turbulento"`

#### Resultado

Debe devolver una cadena de texto indicando el régimen del flujo.

No debe imprimir el resultado.

## 6. Validaciones

- `densidad` debe ser mayor que cero.
- `viscosidad` debe ser mayor que cero.
- El objeto `tuberia` deberá contener un diámetro y un caudal válidos.
- Las entradas serán validadas desde el programa principal antes de crear los objetos.

## 7. Reglas para Copilot

- Implementar únicamente la clase `AnalisisFlujo`.
- Importar la clase `Tuberia` únicamente cuando sea necesario para trabajar con el objeto.
- No duplicar los cálculos de área o velocidad.
- Obtener la velocidad utilizando `self.tuberia.calcular_velocidad()`.
- Obtener el diámetro utilizando `self.tuberia.diametro`.
- Utilizar `self` para acceder a los atributos.
- `clasificar_flujo()` debe reutilizar `calcular_reynolds()`.
- No agregar clases adicionales.
- No agregar atributos que no estén definidos en esta especificación.
- Los métodos deben devolver resultados utilizando `return`.
- Los métodos no deben solicitar datos mediante `input()`.
- Los métodos no deben imprimir resultados.
- No modificar los límites establecidos para la clasificación del flujo.
- No agregar funcionalidades no solicitadas.

## 8. Caso de referencia

Para una tubería con:

- diámetro = 0.050 m
- caudal = 0.002 m**3/s

y un fluido con:

- densidad = 1000 kg/m**3
- viscosidad = 0.001 Pa*s

se espera aproximadamente:

- velocidad = 1.0186 m/s
- número de Reynolds = 50,930
- régimen = Turbulento

Estos valores corresponden al ejercicio original utilizado como referencia del proyecto.