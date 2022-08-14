import networkx as nx
import random as rn
import matplotlib.pyplot as plt
import numpy


def add_nodes(n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G


def add_random_edge(G):
    n = G.order()
    e = G.size()

    max_edges = (n * (n - 1)) / 2

    if e == max_edges:
        return

    nodes = list(G.nodes())

    while 1:
        node1 = rn.choice(nodes)
        node2 = rn.choice(nodes)

        if node1 != node2 and G.has_edge(node1, node2) == 0:
            G.add_edge(node1, node2)
            break

    return G


def add_till_connectivity(G):
    while nx.is_connected(G) == 0:
        G = add_random_edge(G)

    return G


def create_instance(n):
    Gr = add_nodes(n)
    Gr = add_till_connectivity(Gr)
    return Gr.size()


def create_average_instance(n, times):
    results = []

    for i in range(times):
        results.append(create_instance(n))

    return numpy.average(results)


def plot_min_edges_for_connectivity(runs, lower, upper):
    x = []
    y = []

    for i in range(runs):
        n = rn.randint(lower, upper)
        e = create_average_instance(n, 4)

        x.append(n)
        y.append(e)

    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Edges')
    plt.title('Emergence of Connectivity')
    plt.plot(x, y, 'ro')
    plt.show()


def plot_min_edges_for_connectivity(lower, upper):
    x = []
    y = []
    z = []

    for i in range(lower, upper+1, 10):
        x.append(i)
        y.append(create_average_instance(i, 100))
        z.append(i * float(numpy.log(i))/2)

    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Edges')
    plt.title('Emergence of Connectivity')
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()


plot_min_edges_for_connectivity(10, 400)
