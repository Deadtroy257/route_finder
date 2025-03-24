# Sistema Inteligente de Rutas

Este proyecto implementa un sistema inteligente para encontrar la mejor ruta entre dos puntos en un sistema de transporte masivo utilizando programación lógica con Prolog y Python.

## Descripción

El sistema utiliza una base de conocimiento en Prolog para representar las conexiones entre estaciones y aplicar reglas lógicas para encontrar la ruta óptima (de menor costo) entre un punto de origen y un punto de destino.

## Estructura del Proyecto

- `route_finder.py`: Implementación principal del sistema en Python
- `graph_data.py`: Datos del grafo de conexiones entre estaciones
- `rules.pl`: Reglas de Prolog para encontrar la mejor ruta
- `temp_rules.pl`: Archivo temporal generado durante la ejecución (ignorado en git)

## Requisitos

- Python 3.8+
- PySwip (Python interface for SWI-Prolog)
- SWI-Prolog

## Instalación

1. Instalar SWI-Prolog desde [https://www.swi-prolog.org/download/stable](https://www.swi-prolog.org/download/stable)
2. Instalar PySwip: pip install pyswip


## Uso

Para ejecutar el sistema: python route_finder.py


Por defecto, el sistema buscará la mejor ruta desde el punto 'a' hasta el punto 'd'. Para cambiar los puntos de origen y destino, modifique las variables `origen` y `destino` en el archivo `route_finder.py`.

## Ejemplo de Salida

Prolog instance created
Rules loaded successfully
Executing query: mejor_ruta(a, d, Camino, Costo)
Query result: [{'Camino': ['a', 'e', 'f', 'd'], 'Costo': 8}]
La mejor ruta de a a d es: ['a', 'e', 'f', 'd']
Con un costo total de: 8


## Funcionamiento

El sistema funciona en dos partes principales:

1. **Base de conocimiento en Prolog**: Define las conexiones entre estaciones y las reglas para encontrar rutas.
   - `conexion/3`: Hechos que representan las conexiones directas entre estaciones y sus costos.
   - `ruta/4`: Regla recursiva que construye rutas entre estaciones.
   - `mejor_ruta/4`: Regla que encuentra la ruta de menor costo.

2. **Interfaz en Python**: Utiliza PySwip para consultar la base de conocimiento y presentar los resultados.
   - Carga dinámicamente las conexiones desde `graph_data.py`.
   - Combina las reglas base con las conexiones.
   - Ejecuta la consulta Prolog para encontrar la mejor ruta.

## Autor

Estudiante de Ingenieria de Software
Universidad Iberoamericana
8vo Semestre