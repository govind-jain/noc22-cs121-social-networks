from audioop import reverse
import networkx as nx
import random as rn
import numpy as np


# We cannot run loop n^2/2 because the graph is directed
def create_directed_graph_with_probability(n, p):

    G = nx.DiGraph()

    for i in range(n):
        G.add_node(i)

    nodes = G.nodes()

    for u in nodes:
        for v in nodes:
            if u!=v and rn.uniform(0, 1) <= p:
                G.add_edge(u, v)
    
    return G


def random_walk(G, mul):
    nodes = list(G.nodes())
    random_walk_points = [0 for i in range(len(nodes))]

    focus = rn.choice(nodes)

    counter = 0
    limit = mul * G.order()

    while(counter < limit):
        random_walk_points[(int)(focus)] += 1

        out_neighbors = list(G.out_edges(focus))

        if(len(out_neighbors) == 0):
            focus = rn.choice(nodes)
        else:
            chosen_neighbor = rn.choice(out_neighbors)
            focus = chosen_neighbor[1]

        counter += 1
    
    return random_walk_points


def get_nodes_sorted_by_points(points):
    points_array = np.array(points)
    points_sorted_list = np.argsort(-points_array)
    return points_sorted_list


def main():
    G = create_directed_graph_with_probability(10, 0.3)

    random_walk_points = random_walk(G, 5000)    
    nodes_sorted_by_points = get_nodes_sorted_by_points(random_walk_points)
    print(nodes_sorted_by_points)

    page_rank = nx.pagerank(G)
    page_rank_sorted = sorted(page_rank.items(), key = lambda x:x[1], reverse=1)
    list_page_rank_sorted = []

    for el in page_rank_sorted:
        list_page_rank_sorted.append(el[0])
    
    print(list_page_rank_sorted)


main()