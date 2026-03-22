# Aprendiendo Flet

## Proyecto: Calculadora Cambiaria (Flet + Python)

Con este repositorio busco documentar mi proceso de aprendizaje con el framework **Flet**, con el objetivo final de desarrollar una herramienta de cálculo cambiario optimizada para el contexto venezolano.
Inspiración: [Al Cambio App](https://play.google.com/store/apps/details?id=com.alcambio.app&hl=es_VE)

## Idea principal
Desarrollar una aplicación móvil y web de conversión de divisas, pero enfocada en la **velocidad de usuario** sin publicidad que interrumpa el proceso, y pudiendo calcular varias tasas cambiarias a la vez. 

### 🚀 Objetivos 
- **Cálculo en Tiempo Real:** Implementación de funciones para conversiones instantáneas entre divisas.
- **Interfaz Limpia:** Diseño minimalista centrado en la utilidad para cálculos rápidos.

## 📖 Ruta

### Vs 1.0.0 (Publicada)

- Actualmente explorando la [documentación oficial de Flet](https://docs.flet.dev/)

    Avances:
    * Creación de Calculadora en Flet con Personalización
        Bugs resueltos:
        * Se elimina limitación de 4 decimales en los resultados
        * Evita operaciones con cero a la izquierda Ej. 12/03 pasa a 12/3
        * Doble punto 3..2 no permitido
    * APK Generado
    * Release v1.0.0 Publicado

### Vs 1.1 (Publicada)

    * Cambio de Ico
    * Refrescamiento de respuesta táctil
    * Empaquetado independiente de APK por arquitectura 
    ![alt text](img/image-3.png)
    * Comportamiento Responsivo
    ![alt text](img/image.png)
    ![alt text](img/image-1.png)
    ![alt text](img/image-2.png)



### Vs 1.2 (En curso)

    * Se puede interactuar con el panel de la calculadora 
    * Agregado de botón Delete (Retroceso) para borrar números

#### En curso / Fix

    * Al usar botón borrar en un símbolo, borra todos los símbolos dentro de la operación
    * Agregar portapapeles al resultado


### Siguientes pasos:
- Manejo de entradas de usuario (TextFields) para montos.
- Conexión con API o Web Scrapping para obtener las tasas de cambio.
- Maquetado de interfaz.
- Actualización dinámica de etiquetas (Text) para resultados.
- Diseño para que la app funcione en móviles.
