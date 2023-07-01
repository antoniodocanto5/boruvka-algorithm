# Este codigo teve como referencia a pagina web NetworkX que demonstra a implementação
# de grafos ponderados em python com a sua biblioteca
# URL: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html#sphx-glr-auto-examples-drawing-plot-weighted-graph-py

# Codigo responsável para implementar o algoritmo de Boruvka e apresentá-lo graficamente

# Code edited by Marco da Costa, António Canto and Carlos Monteiro
# Este codigo foi editado e adaptado por Marco da Costa, António Canto and Carlos Monteiro
# Análise e Síntese de Algortimos, UniCV 2023

import matplotlib.pyplot as plt
import networkx as nx
from boruvka_algorithm import Graph
import timeit

#
g = Graph(5)


# # #melhor caso
# u = [0,1,1,2]
# v = [1,4,3,4]
# w = [6,4,3,1]
#
#
# # #caso intermedio
# u = [0,0,0,1,1,3,2]
# v = [1,2,4,4,3,4,4]
# w = [6,8,9,4,3,7,1]


# #pior caso
u = [0,0,0,0,1,1,1,2,3,2]
v = [1,2,3,4,4,2,3,3,4,4]
w = [6,8,2,9,4,5,3,7,7,1]


#
for i in range(len(u)):
    g.addEdge(u[i],v[i], w[i])


G = nx.Graph()

#
for i in range(len(u)):
    G.add_edge(u[i], v[i], weight= w[i])

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 6]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 6]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()

#Receber as arestas que pertencem a AGM
uMST, vMST, wMST = g.boruvkaMST()

# Desenhar o grafo AGM
MST = nx.Graph()

#
for i in range(len(uMST)):
    MST.add_edge(uMST[i], vMST[i], weight=wMST[i])

elarge = [(u, v) for (u, v, d) in MST.edges(data=True) if d["weight"] > 6]
esmall = [(u, v) for (u, v, d) in MST.edges(data=True) if d["weight"] <= 6]

pos = nx.spring_layout(MST, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(MST, pos, node_size=700)

# edges
nx.draw_networkx_edges(MST, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    MST, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(MST, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(MST, "weight")
nx.draw_networkx_edge_labels(MST, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()