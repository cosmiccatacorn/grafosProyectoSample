import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r"files/aristas_formato_proyecto_utf8.csv", encoding="utf-8")
#print(df.describe())
#print(df.columns)

edges = list(zip(df['id_inicio'], df['id_fin'], df['distancia']))

G = nx.Graph()
G.add_weighted_edges_from(edges)


def shortest_path(nodeA, nodeB):
    path = nx.dijkstra_path(G, nodeA, nodeB, weight='weight')
    distance = nx.dijkstra_path_length(G, nodeA, nodeB, weight='weight')
    print("Camino: " , "-->".join(path))
    print(f"Distancia: {distance}")
    return path, distance


def visualizar_grafo(grafo):
    G = nx.Graph()

    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(16, 10))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=9)
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas, font_size=7)
    plt.title("Mapa de la Universidad")
    plt.show()
# Obtener lista de nodos
nodes = list(G.nodes)

print(nodes)
a = input("Ingrese el punto de inicio: ")
b = input("Ingrese el punto de fin: ")

try:
    shortest_path(a, b)
except nx.NetworkXNoPath:
    print("No existe un camino que conencte a estos edificios")


