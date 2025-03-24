from pyswip import Prolog
from graph_data import TRANSPORT_GRAPH
import os

def generate_prolog_rules():
    rules = []
    for start, end, cost in TRANSPORT_GRAPH['connections']:
        rules.append(f"conexion({start}, {end}, {cost}).")
    return "\n".join(rules)

def search_best_route(initial_point, final_point):
    try:
        prolog = Prolog()
        print("Prolog instance created")
        
        # Create a temporary file with the rules
        rules_file = "temp_rules.pl"
        
        # Load base rules from file
        with open("rules.pl", "r") as f:
            base_rules = f.read()
        
        # Write combined rules to temporary file
        with open(rules_file, "w") as f:
            f.write(base_rules + "\n" + generate_prolog_rules())
        
        # Consult the file directly
        prolog.consult(rules_file)
        print("Rules loaded successfully")
        
        query = f"mejor_ruta({initial_point}, {final_point}, Camino, Costo)"
        print(f"Executing query: {query}")
        
        consulta = list(prolog.query(query))
        print(f"Query result: {consulta}")
          
        # Clean up temporary file
        os.remove(rules_file)
        
        if not consulta:
            return None, None
        
        mejor_solucion = consulta[0]
        camino = mejor_solucion["Camino"]
        costo = mejor_solucion["Costo"]
        
        return camino, costo
    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None

if __name__ == "__main__":
    origen = 'a'
    destino = 'd'
    mejor_camino, mejor_costo = search_best_route(origen, destino)
    
    if mejor_camino:
        print(f"La mejor ruta de {origen} a {destino} es: {mejor_camino}")
        print(f"Con un costo total de: {mejor_costo}")
    else:
        print(f"No se encontró una ruta de {origen} a {destino}.")