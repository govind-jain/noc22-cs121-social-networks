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


def set_path_colors(G, myopic_path, optimal_path, src, dest):

    colors = []
    nodes = G.nodes()

    myopic_path_set = set(myopic_path)
    optimal_path_set = set(optimal_path)

    for node in nodes:

        if node == src or node == dest:
            colors.append('red')
        elif (node in myopic_path_set) and (node in optimal_path_set):
            colors.append('#7b2f0e') # Copper shade
        elif node in myopic_path_set:
            colors.append('blue')
        elif node in optimal_path_set:
            colors.append('green')
        else:
            colors.append('black')

    return colors


def plot_myopic_and_optimal_paths(G, H, src, dest):

    myopic_path = get_myopic_path(G, H, src, dest)
    optimal_path = nx.shortest_path(G, source=src, target=dest)

    colors = set_path_colors(G, myopic_path, optimal_path, src, dest)
    
    print('Myopic path:', myopic_path)
    print('Optimal path:', optimal_path)

    nx.draw(G, node_color=colors)
    plt.show()


def compare_myopic_and_optimal_paths(G, H):

    n = G.number_of_nodes()

    max_diameter_possible = (int)(n/2)
    diametrically_opposite_pairs = (int)(n/2)

    # For each node there exist two nodes at distance max_diameter_possible
    if n%2 == 1:
        diametrically_opposite_pairs *= 2

    x_axis = []
    myopic_path_len = []
    optimal_path_len = []
    time = 0

    for src in range(0, diametrically_opposite_pairs + 1):

        dest = (src + max_diameter_possible)%n

        myopic_path = get_myopic_path(G, H, src, dest)
        optimal_path = nx.shortest_path(G, source=src, target=dest)

        x_axis.append(time)
        time += 1

        myopic_path_len.append(len(myopic_path))
        optimal_path_len.append(len(optimal_path))

    plt.plot(x_axis, myopic_path_len, 'r')
    plt.plot(x_axis, optimal_path_len, 'b')
    plt.show()
