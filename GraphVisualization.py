#!pip install networkx

import networkx as nx
import matplotlib.pyplot as plt
# Create a graph from the adjacency list
G = nx.Graph()
for node, neighbours in adj_list.items():
    for neighbour in neighbours:
        G.add_edge(node, neighbour)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_size=14, font_weight='bold')
plt.title('Graph Visualization')
plt.show()
