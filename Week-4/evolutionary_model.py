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


def visualize_graph_size_color(G, nsize, ncolor):
    nx.draw(G, node_size=nsize, node_color=ncolor)
    plt.show()


def assign_bmi(G):
    for each in G.nodes():
        G._node[each]['name'] = rn.randint(15, 40)
        G._node[each]['type'] = 'person'


def assign_foci(G):

    n = G.order()
    foci_elements = ['gym', 'canteen', 'table_tennis', 'dance_club', 'nso', 'ncc']

    for i in range(len(foci_elements)):
        idx = n + 1 + i
        G.add_node(idx)
        G._node[idx]['name'] = foci_elements[i]
        G._node[idx]['type'] = 'foci'


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


def get_node_colors(G):
    node_colors = []

    for el in G.nodes():
        if G._node[el]['type'] == 'person':
            node_colors.append('Green')
        else:
            node_colors.append('Red')

    return node_colors


def get_foci_elements(G):
    foci_elements = []

    for el in G.nodes():
        if G._node[el]['type'] == 'foci':
            foci_elements.append(el)

    return foci_elements


def add_edges_to_foci(G):
    foci_elements = get_foci_elements(G)

    for el in G.nodes():
        if G._node[el]['type'] == 'person':
            G.add_edge(el, rn.choice(foci_elements))

    return G


G = create_graph(100)

assign_bmi(G)
assign_foci(G)

label_dict = get_label_dict(G)
node_size = get_node_size(G)
node_colors = get_node_colors(G)

G = add_edges_to_foci(G)

visualize_graph_size_color(G, node_size, node_colors)
