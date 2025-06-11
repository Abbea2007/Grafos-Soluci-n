import heapq

def dijkstra(graph, start):
    #   Inicializar distancias y la cola de prioridad
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        #   Si encontramos una distancia mejor, saltamos
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            #   Si encontramos una ruta mas corta al vecino
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def shortest_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    current = end

    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]

    if path:
        path.insert(0, start)

    return path, distances[end]

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

camino, distancia = shortest_path(graph, 'A', 'E')

print("Camino mas corto:", " -> ".join(camino))
print(f"Tiempo total de viaje: {distancia} minutos")