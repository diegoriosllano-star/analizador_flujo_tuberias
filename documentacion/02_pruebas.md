# 02. Pruebas y validación

## Objetivo

Comprobar que la aplicación realiza correctamente los cálculos del área, velocidad y número de Reynolds, clasifica adecuadamente el régimen del flujo, valida los datos de entrada y almacena los análisis realizados en el historial.

---

## Caso 1. Ejercicio original de Mecánica de Fluidos

### Identificador
Caso 1 - Problema original

### Objetivo
Comprobar que la aplicación reproduce los resultados obtenidos previamente en el ejercicio original de Mecánica de Fluidos.

### Entradas
- Diámetro: 0.050 m
- Caudal: 0.002 m**3/s
- Densidad: 1000 kg/m**3
- Viscosidad: 0.001 Pa*s

### Resultado esperado
- Área: aproximadamente 0.0019635 m**2
- Velocidad: aproximadamente 1.0186 m/s
- Número de Reynolds: aproximadamente 50,929.58
- Régimen: Turbulento

### Resultado obtenido
- Área: 0.0019635 m²
- Velocidad: 1.0186 m/s
- Número de Reynolds: 50929.58
- Régimen: Turbulento

### Estado
Aprobado.

### Observaciones
Los resultados obtenidos coinciden con el ejercicio original de Mecánica de Fluidos utilizado como referencia.

---

## Caso 2. Flujo laminar

### Identificador
Caso 2 - Flujo laminar

### Objetivo
Comprobar que la aplicación identifica correctamente un número de Reynolds menor que 2300.

### Entradas
- Diámetro: 0.050 m
- Caudal: 0.00005 m**3/s
- Densidad: 1000 kg/m**3
- Viscosidad: 0.001 Pa*s

### Resultado esperado
- Área: aproximadamente 0.0019635 m**2
- Velocidad: aproximadamente 0.0255 m/s
- Número de Reynolds: aproximadamente 1,273.24
- Régimen: Laminar

### Resultado obtenido
- Área: 0.0019635 m²
- Velocidad: 0.0255 m/s
- Número de Reynolds: 1273.24
- Régimen: Laminar

### Estado
Aprobado.

### Observaciones
El programa identificó correctamente un flujo laminar al obtener un número de Reynolds menor que 2300.

---

## Caso 3. Valor límite de transición

### Identificador
Caso 3 - Límite Re = 2300

### Objetivo
Comprobar el comportamiento del programa exactamente en el límite inferior del régimen de transición.

### Entradas
- Diámetro: 0.050 m
- Caudal: 0.0001 m**3/s
- Densidad: 1000 kg/m**3
- Viscosidad: 0.001107 Pa*s

### Resultado esperado
- Área: aproximadamente 0.0019635 m**2
- Velocidad: aproximadamente 0.0509 m/s
- Número de Reynolds: aproximadamente 2300.34
- Régimen: Transición

### Resultado obtenido
- Área: 0.0019635 m²
- Velocidad: 0.0509 m/s
- Número de Reynolds: 2300.34
- Régimen: Transición

### Estado
Aprobado.

### Observaciones
El resultado obtenido coincide con el resultado esperado y confirma correctamente el límite inferior del régimen de transición.

---

## Caso 4. Entrada inválida

### Identificador
Caso 4 - Diámetro igual a cero

### Objetivo
Comprobar que el programa rechaza datos menores o iguales a cero y no realiza los cálculos.

### Entradas
- Diámetro: 0
- Caudal: 0.002 m**3/s
- Densidad: 1000 kg/m**3
- Viscosidad: 0.001 Pa*s

### Resultado esperado

El programa debe mostrar:

`Todos los datos deben ser mayores que cero.`

No debe crear los objetos, realizar cálculos ni agregar el análisis al historial.

### Resultado obtenido
Todos los datos deben ser mayores que cero.

### Estado
Aprobado.

### Observaciones
El programa detectó correctamente la entrada inválida y evitó realizar los cálculos.

---

## Caso 5. Historial de análisis

### Identificador
Caso 5 - Almacenamiento y consulta del historial

### Objetivo
Comprobar que varios análisis válidos se almacenan en una lista y pueden consultarse desde la opción 2 del menú.

### Procedimiento

Realizar primero el Caso 1:

- Diámetro: 0.050 m
- Caudal: 0.002 m**3/s
- Densidad: 1000 kg/m**3
- Viscosidad: 0.001 Pa*s

Después realizar el Caso 2:

- Diámetro: 0.050 m
- Caudal: 0.00005 m**3/s
- Densidad: 1000 kg/m**3
- Viscosidad: 0.001 Pa*s

Finalmente seleccionar:

`2. Mostrar historial de análisis`

### Resultado esperado

El historial debe contener dos registros:

### Análisis 1
- Diámetro: 0.0500 m
- Caudal: 0.002000 m**3/s
- Reynolds: aproximadamente 50,929.58
- Régimen: Turbulento

### Análisis 2
- Diámetro: 0.0500 m
- Caudal: 0.000050 m**3/s
- Reynolds: aproximadamente 1,273.24
- Régimen: Laminar

### Resultado obtenido
El historial mostró correctamente dos análisis registrados.

Análisis 1:
- Diámetro: 0.0500 m
- Caudal: 0.002000 m³/s
- Reynolds: 50929.58
- Régimen: Turbulento

Análisis 2:
- Diámetro: 0.0500 m
- Caudal: 0.000050 m³/s
- Reynolds: 1273.24
- Régimen: Laminar

### Estado
Aprobado.

### Observaciones
La aplicación almacenó correctamente varios análisis en una lista y permitió consultarlos desde la opción 2 del menú.

---

# Conclusión de las pruebas

Después de ejecutar los cinco casos se compararán los resultados obtenidos con los resultados esperados.

Los casos que coincidan se marcarán como `Aprobado`. Si algún resultado no coincide, se revisarán la especificación y la implementación antes de ejecutar nuevamente la prueba.