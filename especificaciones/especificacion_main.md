# Especificación del programa principal

## 1. Objetivo

Controlar la interacción del usuario mediante un menú de consola, solicitar y validar los datos necesarios, crear los objetos de las clases `Tuberia` y `AnalisisFlujo`, mostrar los resultados y almacenar los análisis realizados en un historial.

## 2. Menú principal

El programa deberá mostrar las siguientes opciones:

1. Realizar nuevo análisis
2. Mostrar historial de análisis
0. Salir

El menú deberá repetirse mediante un ciclo hasta que el usuario seleccione la opción `0`.

## 3. Lista de historial

El programa deberá utilizar una lista llamada:

`historial`

La lista comenzará vacía:

`historial = []`

Cada vez que se complete correctamente un análisis, se agregará un registro con los datos ingresados y los resultados obtenidos.

El historial permitirá cumplir con el requisito de utilizar una lista para manejar varios resultados.

## 4. Opción 1. Realizar nuevo análisis

### Datos solicitados

Solicitar al usuario:

- diámetro de la tubería en metros;
- caudal en m**3/s;
- densidad del fluido en kg/m**3;
- viscosidad dinámica en Pa*s.

Todos los datos se convertirán a tipo `float`.

### Validación

Todos los valores deben ser mayores que cero.

Si alguno de los valores es menor o igual a cero:

- mostrar un mensaje indicando que los datos deben ser mayores que cero;
- no crear los objetos;
- no realizar los cálculos;
- regresar al menú principal.

### Creación de objetos

Si los datos son válidos:

1. Crear un objeto de la clase `Tuberia`:

`tuberia = Tuberia(diametro, caudal)`

2. Crear un objeto de la clase `AnalisisFlujo`:

`analisis = AnalisisFlujo(tuberia, densidad, viscosidad)`

## 5. Cálculos

Utilizar los métodos de los objetos para obtener:

- área transversal mediante `tuberia.calcular_area()`;
- velocidad mediante `tuberia.calcular_velocidad()`;
- número de Reynolds mediante `analisis.calcular_reynolds()`;
- régimen mediante `analisis.clasificar_flujo()`.

El programa principal no debe repetir las fórmulas implementadas en las clases.

## 6. Resultados mostrados

Después de realizar el análisis se debe mostrar un resumen con:

- diámetro de la tubería;
- caudal;
- densidad;
- viscosidad;
- área transversal;
- velocidad promedio;
- número de Reynolds;
- régimen del flujo.

Los resultados numéricos deberán presentarse de forma clara y con un número razonable de decimales.

## 7. Registro en el historial

Después de mostrar un análisis válido, agregar a la lista `historial` un registro con:

- diámetro;
- caudal;
- densidad;
- viscosidad;
- área;
- velocidad;
- Reynolds;
- régimen.

Cada análisis válido deberá generar un nuevo registro.

## 8. Opción 2. Mostrar historial

Si `historial` está vacío:

- mostrar un mensaje indicando que aún no existen análisis registrados.

Si existen registros:

- recorrer la lista mediante un ciclo;
- mostrar cada análisis con un número consecutivo;
- presentar sus datos principales y resultados.

## 9. Opción 0. Salir

Cuando el usuario seleccione `0`:

- finalizar el ciclo del menú;
- mostrar un mensaje de salida;
- terminar el programa.

## 10. Opción no válida

Si el usuario selecciona una opción diferente a `0`, `1` o `2`:

- mostrar un mensaje de opción no válida;
- regresar al menú principal.

## 11. Caso original de referencia

Para los datos:

- diámetro = 0.050 m
- caudal = 0.002 m**3/s
- densidad = 1000 kg/m**3
- viscosidad = 0.001 Pa*s

se espera aproximadamente:

- área = 0.0019635 m**2
- velocidad = 1.0186 m/s
- Reynolds = 50,930
- régimen = Turbulento

Estos resultados deberán compararse posteriormente con el ejercicio original de Mecánica de Fluidos.

## 12. Reglas para Copilot

- Implementar el programa principal utilizando las clases especificadas.
- Importar `Tuberia` y `AnalisisFlujo` desde sus módulos correspondientes.
- No repetir en `main.py` las fórmulas que pertenecen a las clases.
- Utilizar un ciclo para mantener activo el menú.
- Utilizar una lista para almacenar el historial.
- Utilizar condiciones para validar entradas y opciones.
- No crear clases adicionales.
- No agregar bibliotecas externas innecesarias.
- No cambiar los nombres de las clases ni de sus métodos.
- No agregar funcionalidades no definidas en esta especificación.
- El programa debe iniciar desde una función `main()`.
- Utilizar:

`if __name__ == "__main__":`

para iniciar la ejecución.