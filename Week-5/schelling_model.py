import networkx as nx
import matplotlib.pyplot as plt


def get2DGraph(N):
    G = nx.grid_2d_graph(N, N)
    pos_dict = dict((n, n) for n in G.nodes())
    labels_dict = dict(((i, j), (i * N + j)) for (i, j) in G.nodes())

    return G, pos_dict, labels_dict


def plot2DGraph(G, pos_dict, labels_dict):
    nx.draw(G, pos_dict, with_labels=0)
    nx.draw_networkx_labels(G, pos_dict, labels=labels_dict)
    plt.show()


def connectDiagonals2DGraph(G, N):
    for (x, y) in G.nodes():
        if x+1 < N:
            if y+1 < N:
                G.add_edge((x, y), (x+1, y+1))
            if y-1 >= 0:
                G.add_edge((x, y), (x+1, y-1))

    return G


N = 10
G, pos_dict, labels_dict = get2DGraph(N)
plot2DGraph(G, pos_dict, labels_dict)
connectDiagonals2DGraph(G, N)
plot2DGraph(G, pos_dict, labels_dict)
