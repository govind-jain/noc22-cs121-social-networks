import networkx as nx
import matplotlib.pyplot as plt
import random as rn


def get_influential_power(G, seeds, p):

    n = G.number_of_nodes()

    infected = set(seeds)
    just_infected = seeds

    while len(infected) < n:

        to_be_infected = {}

        for node in just_infected:
            for neighbor in G.neighbors(node):
                if (neighbor in infected)==0 and (rn.random() <= p):
                    to_be_infected[neighbor] = True

        if len(to_be_infected) == 0:
            break

        infected.update(to_be_infected)
        just_infected = list(to_be_infected)

        print('Just infected:', just_infected)

    return list(infected)


def list_of_random_nodes(G, x):

    random_nodes = {}
    nodes = list(G.nodes())

    while len(random_nodes) < x:

        random_node = rn.choice(nodes)

        if (random_node in random_nodes) == 0:
            random_nodes[random_node] = True
    
    return list(random_nodes)


def main():

    graph_size = 10
    p_edge_addition = 0.4
    G = nx.erdos_renyi_graph(graph_size, p_edge_addition)

    intitially_infected_count = (int)(graph_size/3)
    seeds = list_of_random_nodes(G, intitially_infected_count)
    print('Initially infected list:', seeds)

    p_infection_spread = 0.2
    final_infected_list = get_influential_power(G, seeds, p_infection_spread)
    print('Final infected list:', final_infected_list)

    nx.draw(G, with_labels=True)
    plt.show()


main()