import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

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

##por corregir!
def visualizar_grafo(grafo):
    G = grafo

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(16, 10))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=9)
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas, font_size=7)
    plt.title("Mapa de la Universidad")
    plt.show()
# Obtener lista de nodos
nodes = list(G.nodes)
"""
print(nodes)
a = input("Ingrese el punto de inicio: ")
b = input("Ingrese el punto de fin: ")

try:
    shortest_path(a, b)
except nx.NetworkXNoPath:
    print("No existe un camino que conencte a estos edificios")
"""

app = tk.Tk()
app.title("Buscador de Caminos")
app.geometry("1200x1000")

def buscar():
    origen = inicio.get()
    fin = destino.get()

    if not origen or not fin:
        resultado.set("Debe seleccionar los edificios de origen y destino")
    elif origen == fin:
        resultado.set("El origen y el destino no pueden ser iguales")
    else:
        try:
            path, distance = shortest_path(origen, fin)
            resultado.set(f"Camino: {"-->".join(path)} \nDistancia: {distance}")
        except nx.NetworkXNoPath:
            resultado.set("No existe un camino que conencte a estos edificios")


tk.Label(app, text="Edificio Inicio:").pack(pady=5)
inicio = tk.StringVar()
entrada_inicio = ttk.Combobox(app, textvariable=inicio, width = 20)
entrada_inicio['values'] = ['A', 'B', 'C', 'K', 'H', 'Kioscos', 'P.S', 'P.V', 'CasaG', 'O', 'F', 'Atelier', 'G', 'D1', 'CAF', 'PingPong', 'Mesón', 'Biblioteca', 'Cajero', 'Capilla', 'AdPortas', 'Embarca', 'E1', 'E2', 'D2']
#entrada_inicio.grid(column=1, row=5)
entrada_inicio.pack(pady=5)

tk.Label(app, text="Edificio Destino:").pack(pady=5)
destino = tk.StringVar()
entrada_destino = ttk.Combobox(app, textvariable=destino, width = 20)
entrada_destino['values'] = ['A', 'B', 'C', 'K', 'H', 'Kioscos', 'P.S', 'P.V', 'CasaG', 'O', 'F', 'Atelier', 'G', 'D1', 'CAF', 'PingPong', 'Mesón', 'Biblioteca', 'Cajero', 'Capilla', 'AdPortas', 'Embarca', 'E1', 'E2', 'D2']
#entrada_destino.grid(column=1, row=6)
entrada_destino.pack(pady=5)

tk.Label(app, text="Edificios disponibles:").pack()
tk.Label(app, text=", ".join(G.nodes), wraplength=350, fg="blue").pack()


tk.Button(app, text=f"Buscar camino más corto", command=buscar).pack(pady=10)

resultado = tk.StringVar()
tk.Label(app, textvariable=resultado, wraplength=350, justify="left").pack()


app.mainloop()

visualizar_grafo(G)