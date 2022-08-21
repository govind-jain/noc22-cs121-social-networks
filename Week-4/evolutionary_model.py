import networkx as nx
import matplotlib.pyplot as plt
import random as rn
import math


def create_graph(n):
    G = nx.Graph()

    for i in range(1, n + 1):
        G.add_node(i)

    return G


def visualize_graph(G):
    nx.draw(G)
    plt.show()


def visualize_graph_size(G):
    node_size = get_node_size(G)
    nx.draw(G, node_size=node_size)
    plt.show()


def visualize_graph_size_color(G):
    node_size = get_node_size(G)
    node_colors = get_node_colors(G)
    nx.draw(G, node_size=node_size, node_color=node_colors)
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
        node = G._node[el]

        if node['type'] == 'person':
            value = node['name']

            if value < 18:
                node_colors.append('#00C0F0')
            elif value < 25:
                node_colors.append('Lime')
            elif value < 30:
                node_colors.append('Yellow')
            elif value < 35:
                node_colors.append('Orange')
            else:
                node_colors.append('Red')
        else:
            node_colors.append('#B77729')

    return node_colors


def get_foci_elements(G):
    foci_elements = []

    for el in G.nodes():
        if G._node[el]['type'] == 'foci':
            foci_elements.append(el)

    return foci_elements


def get_person_elements(G):
    person_elements = []

    for el in G.nodes():
        if G._node[el]['type'] == 'person':
            person_elements.append(el)

    return person_elements


def get_common_neighbors(G, u, v):
    neighbors_u = set(G.neighbors(u))
    neighbors_v = set(G.neighbors(v))

    return len(neighbors_u & neighbors_v)


def add_edges_to_foci(G):
    foci_elements = get_foci_elements(G)

    for el in G.nodes():
        if G._node[el]['type'] == 'person':
            G.add_edge(el, rn.choice(foci_elements))

    return G


def homphily(G):
    person_elements = get_person_elements(G)
    n = len(person_elements)

    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(G._node[person_elements[i]]['name'] - G._node[person_elements[j]]['name'])
            prob = float(1) / (1000 + diff)

            if rn.uniform(0, 1) < prob:
                G.add_edge(i, j)

    return G


def closure(G):
    pairs = []
    n = G.order()
    nodes = G.nodes()

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if G.has_edge(i, j) == 0 and (nodes[i]['type'] == 'person' or nodes[j]['type'] == 'person'):
                common_neighbors = get_common_neighbors(G, i, j)
                p_for_each_common_node = 0.01
                p_for_becoming_friends = 1 - math.pow(1 - p_for_each_common_node, common_neighbors)

                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(p_for_becoming_friends)
                pairs.append(temp)

    for pair in pairs:
        if rn.uniform(0, 1) < pair[2]:
            G.add_edge(pair[0], pair[1])

    return G


def social_influence(G):
    foci_nodes = get_foci_elements(G)

    for each in foci_nodes:
        if G._node[each]['name'] == 'gym':
            for neighbor in G.neighbors(each):
                temp = G._node[neighbor]['name']
                if temp > 15:
                    G._node[neighbor]['name'] = temp - 1
        elif G._node[each]['name'] == 'canteen':
            for neighbor in G.neighbors(each):
                temp = G._node[neighbor]['name']
                if temp < 40:
                    G._node[neighbor]['name'] = temp + 1

    return G


G = create_graph(100)

assign_bmi(G)
assign_foci(G)

add_edges_to_foci(G)
visualize_graph_size_color(G)

for loop in range(5):
    homphily(G)
    closure(G)
    social_influence(G)
    visualize_graph_size_color(G)
