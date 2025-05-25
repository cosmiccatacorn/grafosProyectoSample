import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r"files/aristas_formato_proyecto_utf8.csv", encoding="utf-8")
print(df.describe())
print(df.columns)

edges = list(zip(df['id_inicio'], df['id_fin'], df['distancia']))

# Crear grafo no dirigido
G = nx.Graph()
G.add_weighted_edges_from(edges)


def shortest_path(nodeA, nodeB):
    path = nx.dijkstra_path(G, nodeA, nodeB, weight='weight')
    distance = nx.dijkstra_path_length(G, nodeA, nodeB, weight='weight')
    print("Camino: " , "-->".join(path))
    print(f"Distancia: {distance}")
    return path, distance
# Obtener lista de nodos
nodes = list(G.nodes)

print(nodes)
a = input("Ingrese el punto de inicio: ")
b = input("Ingrese el punto de fin: ")

try:
    shortest_path(a, b)
except nx.NetworkXNoPath:
    print("No existe un camino que conencte a estos edificios")


