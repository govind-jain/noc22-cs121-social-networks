import networkx as nx
import matplotlib.pyplot as plt
import random as rn


def add_weak_tie(G, nodeList):

    node1 = rn.choice(nodeList)
    node2 = rn.choice(nodeList)

    while node1==node2 or G.has_edge(node1, node2):
        node1 = rn.choice(nodeList)
        node2 = rn.choice(nodeList)

    G.add_edge(node1, node2)

    return G


def add_weak_ties(G, nodeList, number_of_rewirings_to_be_done):

    n = len(nodeList)

    if(number_of_rewirings_to_be_done > (int)(n*(n-1))/2):
        print('Number of rewirings requested is greater than the possible number of edges.')
        return G

    for i in range(number_of_rewirings_to_be_done):
        G = add_weak_tie(G, nodeList)

    return G


def add_edges_homophily(G, nodes, farthestNeighborDistance):
    
    n = G.number_of_nodes()
    
    if farthestNeighborDistance >= n/2:
        farthestNeighborDistance = n/2

    for idx in range(0, n):
        for offset in range(1, farthestNeighborDistance + 1):
            G.add_edge(nodes[idx], nodes[(idx+offset)%n])
            G.add_edge(nodes[idx], nodes[(idx-offset+n)%n])

    return G


def find_best_neighbor(G, H, current, dest):

    min_dist = G.number_of_nodes()
    best_neighbor = current

    for each in G.neighbors(current):
        
        this_dist = nx.shortest_path_length(H, source=each, target=dest)

        if this_dist < min_dist:
            min_dist = this_dist
            best_neighbor = each
            
    return best_neighbor        


def get_myopic_path(G, H, src, dest):

    path = []

    current = src
    path.append(current)

    while current != dest:
        best_neighbor = find_best_neighbor(G, H, current, dest)
        path.append(best_neighbor)
        current = best_neighbor

    return path
