import networkx as nx
import random as rn


def remove_random_node(G):

    if G.order() == 0:
        return G

    node_to_be_removed = rn.choice(list(G.nodes()))

    G.remove_node(node_to_be_removed)

    return G

def remove_selective_node(G):

    if G.order() == 0:
        return G

    highest_degree = 0
    highest_degree_node = -1

    for node in G.nodes():
        temp = G.degree[node]

        if temp > highest_degree:
            highest_degree = temp
            highest_degree_node = node

    G.remove_node(highest_degree_node)

    return G


def make_disconnected(G):

    steps_for_random_removal = 0
    G1 = G.copy()

    while nx.is_connected(G1):
        G1 = remove_random_node(G1)
        steps_for_random_removal += 1

    print("Steps for random removal is", steps_for_random_removal)

    steps_for_selective_removal = 0
    G2 = G.copy()

    while nx.is_connected(G2):
        G2 = remove_selective_node(G2)
        steps_for_selective_removal += 1

    print("Steps for selective removal is", steps_for_selective_removal)


def main():

    print("##################################")

    G = nx.read_edgelist('facebook_combined.txt')
    print("Results for a real world network")
    make_disconnected(G)

    print("##################################")

    G = nx.erdos_renyi_graph(1000, 0.2)
    print("Results for a random network")
    make_disconnected(G)

    print("##################################")


main()