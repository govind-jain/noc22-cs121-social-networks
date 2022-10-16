import networkx as nx
import matplotlib.pyplot as plt
import random as rn


def get_kshell_decomposition(H):

    G = H.copy()
    
    kshell_decomposition = []
    it = 1

    while G.number_of_nodes() > 0:

        this_shell = []
        
        while 1:
            degrees = G.degree()
            nodes = G.nodes()

            to_be_removed = []

            for node in nodes:
                if degrees[node] <= it:
                    this_shell.append(node)
                    to_be_removed.append(node)

            if len(to_be_removed) == 0:
                break

            for node in to_be_removed:
                G.remove_node(node)

        kshell_decomposition.append(this_shell)
        it += 1
    
    return kshell_decomposition


def add_random_edges(G, m):

    nodes = list(G.nodes())

    while G.number_of_edges() != m:

        node1 = rn.choice(nodes)
        node2 = rn.choice(nodes)

        if node1 != node2 and G.has_edge(node1, node2) == False:
            G.add_edge(node1, node2)
    
    return G


def main():

    n = 10
    m = n

    G = nx.Graph();
    G.add_nodes_from(range(0, n))
    G = add_random_edges(G, m)

    print(get_kshell_decomposition(G))

    nx.draw(G, with_labels=True)
    plt.show()


main()