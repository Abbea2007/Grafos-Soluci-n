import heapq

#Este fragmento de codigo se relaciona con las calles de paris conectadas
#Es un grafo tipo completo ya que todas se relacionan entre si pya que permite devolverse
# Grafo dirigido ponderado (ciudades y distancias)
grafo = {
    'Paris': {'Nancy': 386, 'Lyon': 468},
    'Nancy': {'Lyon': 491},
    'Lyon': {'Marsella': 314, 'Burdeos': 485},
    'Burdeos': {'Toulouse': 224},
    'Toulouse': {},
    'Nantes': {'Paris': 383, 'Burdeos': 338},
    'Marsella': {},
}

def dijkstra(grafo, inicio, fin):
    cola = [(0, inicio, [])]
    visitados = set()

    while cola:
        (costo, actual, camino) = heapq.heappop(cola)

        if actual in visitados:
            continue

        camino = camino + [actual]
        visitados.add(actual)

        if actual == fin:
            return (costo, camino)

        for vecino, peso in grafo.get(actual, {}).items():
            if vecino not in visitados:
                heapq.heappush(cola, (costo + peso, vecino, camino))

    return (float("inf"), [])

# Prueba: encontrar la ruta más corta de Nantes a Marsella
origen = 'Nantes'
destino = 'Marsella'
distancia, ruta = dijkstra(grafo, origen, destino)

print(f"La ruta más corta de {origen} a {destino} es:")
print(" → ".join(ruta))
print(f"Distancia total: {distancia} km")
