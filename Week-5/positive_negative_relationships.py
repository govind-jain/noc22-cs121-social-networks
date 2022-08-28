import networkx as nx
import matplotlib.pyplot as plt
import random as rn
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


G = create_graph(6)
G = add_friendship_edges(G)
display_friendships(G)