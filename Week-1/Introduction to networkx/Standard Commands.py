import networkx as nx
import random as rn
import matplotlib.pyplot as plt

a = "Titilagarh"
b = "Tusra"

# Initialize the Graph
G = nx.Graph()  # Undirected graph
G = nx.DiGraph()  # Directed graph
G.add_node(a)
G.add_edge(a, b)  # ,weight = w

# Get graph data
G.nodes()
G.edges()
G.order()  # Number of nodes
G.size()  # Number of edges

# Find if graph has or not
G.has_edge(a, b)
G.has_node(a)
nx.has_path(G, a, b)

# Draw the graph normally
nx.draw(G)  # ,with_labels = True
plt.show()

# Draw graph by selecting layout
# pos = nx."LayoutName"_layout()
# nx.draw_networkx_edge_labels(G, pos)
# nx.draw(G, pos)
plt.show()
