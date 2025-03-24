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

- Python 3.6+
- PySwip (Python interface for SWI-Prolog)
- SWI-Prolog

## Instalación

1. Instalar SWI-Prolog desde [https://www.swi-prolog.org/download/stable](https://www.swi-prolog.org/download/stable)
2. Instalar PySwip: