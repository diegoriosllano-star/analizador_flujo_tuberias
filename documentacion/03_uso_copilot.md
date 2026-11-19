# 03. Uso de GitHub Copilot

## 1. ¿Cómo utilizaste las especificaciones para solicitar código a Copilot?

Antes de implementar el programa se crearon archivos de especificación para cada clase y para el programa principal.

En estos archivos se definieron las responsabilidades, atributos, constructor, métodos, algoritmos, reglas y validaciones.

Estas especificaciones se utilizaron como referencia para indicar a Copilot qué debía implementar, evitando solicitar toda la aplicación en una sola instrucción.

## 2. ¿Qué revisaste o modificaste del código generado?

Se revisó que el código generado respetara:

- Los nombres de las clases.
- Los atributos definidos.
- Los métodos indicados.
- Las fórmulas del área, velocidad y número de Reynolds.
- Los límites para clasificar el régimen del flujo.
- La validación de entradas.
- El uso de una lista para almacenar el historial.

También se verificó que no se agregaran clases, métodos o funcionalidades que no estuvieran indicadas en las especificaciones.

## 3. ¿Copilot generó una respuesta incorrecta o distinta de lo solicitado?

Durante el desarrollo se revisaron las propuestas antes de aceptarlas.

Cuando una sugerencia no coincidía completamente con lo especificado, se utilizó únicamente la parte que respetaba las reglas definidas o se corrigió antes de integrarla al proyecto.

El objetivo fue mantener el código de acuerdo con las especificaciones diseñadas previamente.

## 4. ¿Cómo comprobaste el funcionamiento de clases y métodos?

Primero se probaron las clases individualmente.

La clase `Tuberia` se comprobó utilizando los datos del ejercicio original para verificar el cálculo del área y la velocidad.

Después se comprobó la clase `AnalisisFlujo` utilizando los mismos datos para verificar el número de Reynolds y la clasificación del régimen.

Finalmente se ejecutó la aplicación completa desde `main.py` y se realizaron cinco casos de prueba documentados.

## 5. ¿Qué ventajas y limitaciones observaste?

Una ventaja de GitHub Copilot es que ayuda a generar código rápidamente a partir de una especificación clara.

También facilita la escritura de estructuras repetitivas y permite comparar propuestas de implementación.

Una limitación es que puede generar código diferente a lo solicitado o agregar funcionalidades innecesarias si la especificación no es suficientemente clara.

Por esta razón es necesario revisar siempre las sugerencias antes de utilizarlas.

## 6. ¿Por qué es necesario comprender código producido con ayuda de IA?

Es necesario comprender el código porque la responsabilidad del funcionamiento del programa sigue siendo del desarrollador.

Comprender el código permite detectar errores, comprobar los cálculos, realizar modificaciones y explicar el funcionamiento de las clases, atributos, métodos y objetos utilizados.

La IA funciona como una herramienta de apoyo, pero no sustituye el análisis y la comprensión del problema.