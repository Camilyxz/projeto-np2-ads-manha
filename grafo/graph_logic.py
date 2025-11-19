#avaliação
def connected(graph, a, b):

    # Verifica existência dos vértices
    if a not in graph or b not in graph:
        return False

    fila = [a]          # fila de BFS
    visitados = [a]     # lista de visitados

    while fila:
        u = fila.pop(0)     # remove o primeiro da fila

        if u == b:
            return True

        for v in graph.get(u, []):
            if v not in visitados:
                visitados.append(v)
                fila.append(v)

    return False
