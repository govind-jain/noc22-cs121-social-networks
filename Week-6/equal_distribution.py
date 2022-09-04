import networkx as nx
import random as rn


# We cannot run loop n^2/2 because the graph is directed
def create_directed_graph_with_probability(n, p):

    G = nx.DiGraph()

    for i in range(1, n+1):
        G.add_node(i)

    nodes = G.nodes()

    for u in nodes:
        for v in nodes:
            if u!=v and rn.uniform(0, 1) <= p:
                G.add_edge(u, v)
    
    return G
