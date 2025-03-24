from graph_data import TRANSPORT_GRAPH, RULES, KNOWLEDGE_BASE
import heapq

def find_best_route(start, end, graph):
    # 1. Construye el grafo como lista de adyacencia
    # Ej: {'a': [('b',5), ('e',3)], 'b': [('c',2), ...], ...}
    graph = graph
    
    # 2. Implementación del algoritmo de Dijkstra usando heap
    heap = []
    heapq.heappush(heap, (0, start, [start]))  # (costo acumulado, nodo actual, camino)
    visited = set()  # Nodos ya procesados
    
    # 3. Procesamiento del heap
    while heap:
        cost, node, path = heapq.heappop(heap)  # Obtiene el nodo con el menor costo acumulado
        
        # 4. Condición de término: encontrar el nodo destino
        if node == end:
            return path, cost  # Devuelve camino completo y costo total
            
        # 5. Evita reprocesar nodos ya visitados
        if node not in visited:
            visited.add(node)
            
            # 6. Explora vecinos del nodo actual
            for neighbor, neighbor_cost in graph.get(node, []):
                if neighbor not in visited:
                    new_cost = cost + neighbor_cost  # Acumula costo
                    new_path = path + [neighbor]     # Extiende camino
                    heapq.heappush(heap, (new_cost, neighbor, new_path))
    
    # 7. Caso sin solución
    return None, None

def apply_rules_to_cost(base_cost, kb=KNOWLEDGE_BASE, rules=RULES):
    """
    Aplica todas las reglas que sean válidas para la base de conocimiento.
    Retorna el costo ajustado.
    """
    cost = base_cost
    for rule_name, rule_data in rules.items():
        # Si la condición de la regla se cumple para la base de conocimiento...
        if rule_data["condition"](kb):
            # ...aplicamos la 'acción' sobre el costo.
            cost = rule_data["action"](cost)
    return cost

def build_graph(connections, kb, rules):
    """
    Construye un diccionario de listas de adyacencia,
    aplicando las reglas al costo base de cada conexión.
    """
    graph = {}
    for s, e, c in connections:
        # Aplica reglas lógicas al costo base 'c'
        adjusted_cost = apply_rules_to_cost(c, kb, rules)
        
        if s not in graph:
            graph[s] = []
        # Agrega la conexión con el costo ajustado
        graph[s].append((e, adjusted_cost))
        
        # En muchos sistemas de transporte podría haber bidireccionalidad:
        # if e not in graph:
        #     graph[e] = []
        # graph[e].append((s, adjusted_cost))
        #
        # Eso depende de si tu grafo es dirigido o no.
    
    return graph

def search_best_route(initial_point, final_point):
    try:
        graph = build_graph(
            TRANSPORT_GRAPH["connections"],
            KNOWLEDGE_BASE,
            RULES
        )
        return find_best_route(initial_point, final_point, graph)
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None


if __name__ == "__main__":
    origen = input("Ingrese el punto de partida: ").lower()
    destino = input("Ingrese el punto de destino: ").lower()
    mejor_camino, mejor_costo = search_best_route(origen, destino)
    
    if mejor_camino:
        print(f"La mejor ruta de ({origen}) hacia ({destino}) es: {mejor_camino}")
        print(f"Con un costo total de: {mejor_costo}")
    else:
        print(f"No se encontró una ruta de ({origen}) hacia ({destino}).")