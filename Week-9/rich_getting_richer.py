import networkx as nx
import matplotlib.pyplot as plt
import random as rn

def display_graph(G, i, ne):

    pos = nx.circular_layout(G)

    if i == '' and ne == '':
        new_node = []
        rest_nodes = G.nodes()
        new_edges = []
        rest_edges = G.edges()
    else:
        new_node = [i]
        rest_nodes = list(set(G.nodes()) - set(new_node))
        new_edges = ne
        rest_edges = list(set(G.edges()) - set(ne) - set([(b, a) for (a,b) in new_edges]))

    nx.draw_networkx_nodes(G, pos, nodelist=new_node, node_color='r')
    nx.draw_networkx_nodes(G, pos, nodelist=rest_nodes, node_color='g')
    nx.draw_networkx_edges(G, pos, edgelist=new_edges, edge_color='r', style='dashdot')
    nx.draw_networkx_edges(G, pos, edgelist=rest_edges, edge_color='g')
    plt.show()


def get_probabilities(G):

    nodes = G.nodes()
    degrees = nx.degree(G)
    sumOfAllDegrees = G.size() * 2

    probabilities = {}

    for node in nodes:
        probabilities[node] = degrees[node]/sumOfAllDegrees

    return probabilities


def get_cumulative_prob(probabilities):

    cumulative_prob = []
    prev = 0

    for n,p in probabilities.items():
        temp = [n, prev + p]
        cumulative_prob.append(temp)
        prev += p

    return cumulative_prob


def add_nodes_barbasi(G, n, m0):

    m = m0 - 1

    for i in range(m0+1, n+1):

        cumulative_prob = get_cumulative_prob(get_probabilities(G))
        G.add_node(i)

        new_edges = []
        num_edges_added = 0
        target_nodes = {}

        while num_edges_added < m:

            r = rn.uniform(0, 1)
            prev = 0
            idx = 0

            while not(r>prev and r<=cumulative_prob[idx][1]):
                prev = cumulative_prob[idx][1]
                idx += 1

            target_node = cumulative_prob[idx][0]

            if target_node in target_nodes:
                continue

            G.add_edge(i, target_node)
            target_nodes[target_node] = True
            new_edges.append((i, target_node))
            num_edges_added += 1

        display_graph(G, i, new_edges)

    return G


def main():

    n = int(input('Enter the value of n.\n'))
    m0 = rn.randint(2, n/5)

    G = nx.path_graph(m0)

    display_graph(G, '', '')

    G = add_nodes_barbasi(G, n, m0)


main()