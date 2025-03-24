# Sistema Inteligente de Rutas

Este proyecto implementa un sistema para encontrar la ruta óptima entre dos puntos en una red de transporte utilizando Python.

## Descripción

El sistema utiliza el algoritmo de Dijkstra para encontrar el camino de menor costo entre un punto de origen y un destino, implementado completamente en Python.

## Estructura del Proyecto

- `route_finder.py`: Implementación del algoritmo de búsqueda de rutas
- `graph_data.py`: Almacena las conexiones entre estaciones y sus costos

## Requisitos

- Python 3.8 o superior
- Módulos estándar de Python (no se requieren instalaciones adicionales)

## Instalación

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
```bash
cd d:\DOCUMENTOS\IBEROAMERICANA\6to_SEMESTRE\INTELIGENCIA_ARTIFICIAL\UNIDAD 2\actividad2

```bash
python route_finder.py
```

## Uso

1. Ejecutar `route_finder.py`.
2. Ingresar el nombre de la estación de origen y destino.
3. El sistema mostrará la ruta óptima y el costo total.

## Ejemplo de Salida
La mejor ruta de A a D es: ['a', 'e', 'f', 'd']
Con un costo total de: 8

## Funcionamiento

El algoritmo de Dijkstra se utiliza para encontrar la ruta más corta entre dos puntos en un grafo ponderado.

El sistema utiliza:

1. Algoritmo de Dijkstra : Para encontrar el camino de menor costo
2. Separación de preocupaciones :
   - graph_data.py : Almacena la estructura del grafo
   - route_finder.py : Contiene la lógica de búsqueda

## Autor
Estudiante de Ingeniería de Software
Universidad Iberoamericana
8vo Semestre