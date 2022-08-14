import networkx as nx
import matplotlib.pyplot as plt


def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples = list(dict1.items())
    list_of_tuples.sort(key=lambda x: x[1], reverse=True)
    return list_of_tuples[0][0]


def girvan_newman(G):
    while nx.is_connected(G):
        G.remove_edge(*edge_to_remove(G))

    nx.draw(G, with_labels=True)
    plt.show()


Gr = nx.barbell_graph(5, 0)
girvan_newman(Gr)

Karate_Club = nx.karate_club_graph()
girvan_newman(Karate_Club)
