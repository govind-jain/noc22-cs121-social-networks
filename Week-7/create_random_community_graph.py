import networkx as nx
import random as rn

def add_cluster(G, st, en):

    nodes = range(st, en+1)

    for i in nodes:
        G.add_node(i)

    for u in nodes:
        for v in nodes:
            if u<v and rn.uniform(0, 1)<0.5:
                G.add_edge(u, v)

    return G


def add_bridge(G, st1, en1, st2, en2):

    u = rn.randint(st1, en1)
    v = rn.randint(st2, en2)

    G.add_edge(u, v)

    return G


def main():
    
    G = nx.Graph()

    G = add_cluster(G, 0, 9)
    G= add_cluster(G, 10, 19)

    G = add_bridge(G, 0, 9, 10, 19)

    nx.write_gml(G, 'random_community_graph.gml')
    

main()
