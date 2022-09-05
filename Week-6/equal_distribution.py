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


def initialize_points(G, point):
    points = []

    for i in range(G.order()):
        points.append(point)

    return points


def point_distribution_iteration(G, prev_points):
    new_points = [0 for i in range(G.order())]

    for node in G.nodes():
        out_edges = G.out_edges(node)

        if(len(out_edges) == 0):
            new_points[node] += prev_points[node]
        else:
            share = (float)(prev_points[node])/len(out_edges)

            for out_edge in out_edges:
                new_points[out_edge[1]] += share

    return new_points


def reached_equilibrium(prev_points, new_points):

    n = len(prev_points)

    for i in range(n):
        change = abs(prev_points[i] - new_points[i])

        if prev_points[i] == 0:
            continue

        change_fraction = ((float)(change)/prev_points[i]) * 100

        if(change_fraction > 1):
            return False

    return True


def handle_points_sink(points, point, f):

    r = 1-f

    for i in range(len(points)):
        points[i] = f*points[i] + r*point

    return points


def point_distribution(G, points, point, f):

    prev_points = points

    while(1):
        new_points = point_distribution_iteration(G, prev_points)

        new_points = handle_points_sink(new_points, point, f)

        if(reached_equilibrium(prev_points, new_points)):
            break

        prev_points = new_points
    
    return new_points


def get_nodes_sorted_by_points(points):
    points_array = np.array(points)
    points_sorted_list = np.argsort(-points_array)
    return points_sorted_list


def main():
    G = create_directed_graph_with_probability(10, 0.3)
    points = initialize_points(G, 100)

    points = point_distribution(G, points, 100, 0.8)

    points_sorted_list = get_nodes_sorted_by_points(points)
    print(points_sorted_list)

    page_rank = nx.pagerank(G)
    page_rank_sorted = sorted(page_rank.items(), key = lambda x:x[1], reverse=1)
    
    for el in page_rank_sorted:
        print(el[0])


main()