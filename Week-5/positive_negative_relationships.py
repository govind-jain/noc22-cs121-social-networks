import networkx as nx
import matplotlib.pyplot as plt
import random as rn
import itertools


def create_graph(N):
    G = nx.Graph()

    for i in range(1, N + 1):
        G.add_node(i)

    newLabels = {1: "Madhuri", 2: "Juhi", 3: "Kajol", 4: "Raveena", 5: "Shilpa",
                 6: "Hema", 7: "Rekha", 8: "Jaya", 9: "Sushma", 10: "Kareena",
                 11: "Katrina", 12: "Priyanka", 13: "Rashmika", 14: "Samantha"}

    G = nx.relabel_nodes(G, newLabels)

    return G


def add_friendship_edges(G):
    signs = ['+', '-']

    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                G.add_edge(i, j, sign=rn.choice(signs))

    return G


def display_friendships(G):
    pos = nx.circular_layout(G)
    relationships = nx.get_edge_attributes(G, 'sign')

    nx.draw(G, pos, with_labels=True, node_size=5000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=relationships, font_size=20, font_color='red')
    plt.show()


def get_list_of_all_triangles(G):
    nodes = G.nodes()
    all_triangles = [list(x) for x in itertools.combinations(nodes, 3)]
    return all_triangles


def get_list_of_all_unstable_triangles(G, all_triangles):
    unstable_triangles = []

    for triangle in all_triangles:
        minus = 0

        if G[triangle[0]][triangle[1]]['sign'] == '-':
            minus += 1

        if G[triangle[1]][triangle[2]]['sign'] == '-':
            minus += 1

        if G[triangle[2]][triangle[0]]['sign'] == '-':
            minus += 1

        if minus == 1 or minus == 3:
            unstable_triangles.append(triangle)

    return unstable_triangles


def stabilize_one_triangle(G, unstable_triangles):
    triangle_to_be_stabilized = rn.choice(unstable_triangles)

    relation_to_be_flipped = rn.randint(0, 2)

    node1 = triangle_to_be_stabilized[relation_to_be_flipped]
    node2 = triangle_to_be_stabilized[(relation_to_be_flipped + 1) % 3]

    if G[node1][node2]['sign'] == '+':
        G[node1][node2]['sign'] = '-'
    else:
        G[node1][node2]['sign'] = '+'

    return G


def stabilize_all_triangles(G):
    all_triangles = get_list_of_all_triangles(G)

    unstable_triangles = get_list_of_all_unstable_triangles(G, all_triangles)

    while len(unstable_triangles) != 0:
        G = stabilize_one_triangle(G, unstable_triangles)
        unstable_triangles = get_list_of_all_unstable_triangles(G, all_triangles)

    return G


G = create_graph(6)
G = add_friendship_edges(G)
display_friendships(G)

G = stabilize_all_triangles(G)
display_friendships(G)
