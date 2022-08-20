import networkx as nx
import matplotlib.pyplot as plt
import random as rn


def create_graph(n):
    G = nx.Graph()

    for i in range(1, n+1):
        G.add_node(i)

    return G


def visualize_graph(G):
    nx.draw(G)
    plt.show()


def visualize_graph_size(G, nsize):
    nx.draw(G, node_size=nsize)
    plt.show()


def assign_bmi(G):
    for each in G.nodes():
        G._node[each]['name'] = rn.randint(15, 40)
        G._node[each]['type'] = 'person'


def get_label_dict(G):
    label_dict = {}

    for el in G.nodes():
        label_dict[el] = G._node[el]['name']

    return label_dict


def get_node_size(G):
    node_size = []

    for el in G.nodes():
        if G._node[el]['type'] == 'person':
            node_size.append(G._node[el]['name'] * 20)
        else:
            node_size.append(1000)

    return node_size


G = create_graph(100)

assign_bmi(G)

label_dict = get_label_dict(G)
node_size = get_node_size(G)

visualize_graph_size(G, node_size)
