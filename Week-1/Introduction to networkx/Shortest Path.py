import networkx as nx
import random as rn
import matplotlib.pyplot as plt
import sys


def add_random_edge(G, costs):
    cityList = list(G.nodes())
    nodeA = rn.choice(cityList)
    nodeB = rn.choice(cityList)

    if nodeA != nodeB and G.has_edge(nodeA, nodeB) == 0:
        cost = rn.choice(costs)
        G.add_edge(nodeA, nodeB, weight=cost)


def add_nodes_to_graph(G, nodes):
    for node in nodes:
        G.add_node(node)


def shortestPath(G, cityA, cityB):
    try:
        distance = nx.dijkstra_path_length(G, cityA, cityB)
    except:
        distance = 10000

    return distance


cities = ["Titilagarh", "Balangir", "Tusra", "Sambalpur"]
costs = [70, 55, 120, 35, 85]

G = nx.Graph()
add_nodes_to_graph(G, cities)

cityA = "Titilagarh"
cityB = "Tusra"

x = []
y = []

for time in range(11):
    add_random_edge(G, costs)
    x.append(time)
    y.append(shortestPath(G, cityA, cityB))

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Shortest Path")
plt.show()
