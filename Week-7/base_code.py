import networkx as nx
import matplotlib.pyplot as plt
import random as rn

def set_all_A(G):

    for each in G.nodes():
        G._node[each]['action'] = 'A'
    
    return G


def set_selected_B(G, listB):

    for each in listB:
        G._node[each]['action'] = 'B'

    return G


def get_colors(G):

    colors = []

    for each in G.nodes():
        if G._node[each]['action'] == 'A':
            colors.append('green')
        elif G._node[each]['action'] == 'B':
            colors.append('red')

    return colors


def print_graph(G):
    
    colors = get_colors(G)

    nx.draw(G, with_labels=True, node_color=colors, node_size=800)
    plt.show()


def find_neighbour(id, char, G):
    
    count = 0
    neighbors = G.neighbors(id)

    for adj in neighbors:
        if G._node[adj]['action'] == char:
            count += 1
    
    return count


def next_iteration_values(G):

    nodes = G.nodes()

    payoff_A = 5
    payoff_B = 12

    new_results = {}

    for each in nodes():
        count_A = find_neighbour(each, 'A', G)
        count_B = find_neighbour(each, 'B', G)

        overall_payoff_A = count_A * payoff_A
        overall_payoff_B = count_B * payoff_B

        if overall_payoff_A > overall_payoff_B:
            new_results[each] = 'A'
        elif overall_payoff_A < overall_payoff_B:
            new_results[each] = 'B'
        else:
            new_results[each] = rn.choice(['A', 'B'])

    return new_results


def recalculate_options(G):

    new_results = next_iteration_values(G)
    nodes = G.nodes()

    for each in nodes:
        G._node[each]['action'] = new_results[each]
    
    return G


def all_nodes_same_action(G):

    n = G.order()
    nodes = G.nodes()

    count_A = 0

    for each in nodes:
        if G._node[each]['action'] == 'A':
            count_A += 1

    if count_A==n or count_A==0:
        return True

    return False


def main():
    G = nx.erdos_renyi_graph(10, 0.5)
    G = set_all_A(G)

    listB = [0, 1]
    G = set_selected_B(G, listB)

    print_graph(G)

    count = 0
    flag = False

    while(1):

        if count >= 100:
            break

        flag = all_nodes_same_action(G)

        if flag:
            break

        G = recalculate_options(G)
        # print_graph(G)

        count += 1

    if flag:
        print("Cascade is completed")
    else:
        print("Cascade is not completed")

    print_graph(G)


main()
