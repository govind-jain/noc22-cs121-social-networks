import networkx as nx
import random as rn
import matplotlib.pyplot as plt

cities = ["Titilagarh", "Balangir", "Tusra", "Sambalpur"]
costs = [70, 55, 120, 35, 85]

G = nx.Graph()

for city in cities:
    G.add_node(city)

# while G.number_of_edges() < 5:
while G.size() < 5:
    nodeA = rn.choice(cities)
    nodeB = rn.choice(cities)

    if nodeA != nodeB and G.has_edge(nodeA, nodeB) == 0:
        cost = rn.choice(costs)
        G.add_edge(nodeA, nodeB, weight=cost)

pos = nx.circular_layout(G)
nx.draw(G, with_labels=True)
nx.draw_networkx_edge_labels(G, pos)
plt.show()
