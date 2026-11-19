# Especificación de la clase Tuberia

## 1. Nombre de la clase

`Tuberia`

## 2. Objetivo y responsabilidad

Representar una tubería circular y almacenar los datos necesarios para calcular su área transversal y la velocidad promedio del fluido.

La clase será responsable únicamente de los cálculos relacionados con la geometría de la tubería y el caudal.

## 3. Atributos

### diametro
- Tipo: `float`
- Unidad: metros (m)
- Significado: diámetro interior de la tubería.
- Restricción: debe ser mayor que cero.

### caudal
- Tipo: `float`
- Unidad: metros cúbicos por segundo (m**3/s)
- Significado: volumen de fluido que circula por unidad de tiempo.
- Restricción: debe ser mayor que cero.

## 4. Constructor

### `__init__(self, diametro, caudal)`

Recibe:

- `diametro`
- `caudal`

Debe guardar los valores en:

- `self.diametro`
- `self.caudal`

No debe realizar cálculos dentro del constructor.

## 5. Métodos

### `calcular_area(self)`

#### Objetivo
Calcular el área transversal de la tubería.

#### Atributos utilizados
- `self.diametro`

#### Algoritmo

Utilizar la fórmula:

A = πD**2 / 4

donde:

- A = área transversal.
- D = diámetro interior.

#### Resultado

Debe devolver un valor `float` correspondiente al área en m**2.

No debe imprimir el resultado.


### `calcular_velocidad(self)`

#### Objetivo
Calcular la velocidad promedio del fluido dentro de la tubería.

#### Atributos utilizados
- `self.caudal`
- `self.diametro`

#### Algoritmo

1. Obtener el área utilizando `calcular_area()`.
2. Calcular:

V = Q / A

donde:

- V = velocidad promedio.
- Q = caudal.
- A = área transversal.

#### Resultado

Debe devolver un valor `float` correspondiente a la velocidad en m/s.

No debe imprimir el resultado.

## 6. Validaciones

- `diametro` debe ser mayor que cero.
- `caudal` debe ser mayor que cero.
- La validación de los datos de entrada se realizará desde el programa principal antes de crear el objeto.

## 7. Reglas para Copilot

- Implementar únicamente la clase `Tuberia`.
- No agregar clases adicionales.
- No agregar atributos diferentes a `diametro` y `caudal`.
- Utilizar `self` para acceder a los atributos.
- Utilizar `math.pi` para el cálculo del área.
- `calcular_velocidad()` debe reutilizar `calcular_area()`.
- No duplicar la fórmula del área dentro de `calcular_velocidad()`.
- Los métodos deben devolver resultados mediante `return`.
- Los métodos no deben utilizar `input()`.
- Los métodos no deben imprimir resultados.
- No agregar funcionalidades que no estén definidas en esta especificación.

## 8. Caso de referencia

Para:

- diámetro = 0.050 m
- caudal = 0.002 m**3/s

se espera aproximadamente:

- área = 0.0019635 m**2
- velocidad = 1.0186 m/s

Estos valores corresponden al ejercicio original utilizado como referencia del proyecto.