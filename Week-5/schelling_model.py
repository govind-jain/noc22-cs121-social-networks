import networkx as nx
import matplotlib.pyplot as plt
import random as rn


def get_2D_graph(N):
    G = nx.grid_2d_graph(N, N)
    pos_dict = dict((n, n) for n in G.nodes())
    labels_dict = dict(((i, j), (i * N + j)) for (i, j) in G.nodes())

    return G, pos_dict, labels_dict


def get_colors_dict(G):
    colors_dict = []

    for each in G.nodes():
        node_type = G._node[each]['type']

        if node_type == 0:
            colors_dict.append('#00BFFF')
        elif node_type == 1:
            colors_dict.append('#00FF00')
        else:
            colors_dict.append('#FF0000')

    return colors_dict


def plot_2D_graph(G, pos_dict, labels_dict):
    nx.draw(G, pos_dict, with_labels=0)
    nx.draw_networkx_labels(G, pos_dict, labels=labels_dict)

    plt.show()


def plot_2D_graph_colors(G, pos_dict, labels_dict):
    colors_dict = get_colors_dict(G)

    nx.draw(G, pos_dict, node_color=colors_dict, with_labels=0)
    nx.draw_networkx_labels(G, pos_dict, labels=labels_dict)

    plt.show()


def connect_diagonals_2D_graph(G, N):
    for (x, y) in G.nodes():
        if x+1 < N:
            if y+1 < N:
                G.add_edge((x, y), (x+1, y+1))
            if y-1 >= 0:
                G.add_edge((x, y), (x+1, y-1))

    return G


def assign_type(G):

    for cell in G.nodes():
        cell_type = rn.randint(0, 2)
        G._node[cell]['type'] = cell_type

    return G


def is_unsatisfied(G, element):
    threshold = 3
    neighbors = list(G.neighbors(element))

    if len(neighbors) < threshold:
        return True

    node_type = G._node[element]['type']
    similar = 0

    for neighbor in neighbors:
        if node_type == G._node[neighbor]['type']:
            similar += 1

    return similar < threshold


def shift_unsatisfied_node(G, labels_dict, unsatisfied_node, empty_cell):
    G._node[empty_cell]['type'] = G._node[unsatisfied_node]['type']
    G._node[unsatisfied_node]['type'] = 0
    labels_dict[unsatisfied_node], labels_dict[empty_cell] = labels_dict[empty_cell], labels_dict[unsatisfied_node]

    return G, labels_dict


def rearrange_a_unsatisfied_node(G, labels_dict):
    unsatisfied_nodes = []
    empty_cells = []

    for element in G.nodes():
        node_type = G._node[element]['type']

        if node_type == 0:
            empty_cells.append(element)
        elif is_unsatisfied(G, element):
            unsatisfied_nodes.append(element)

    if len(empty_cells) == 0:
        return G, labels_dict, 0
    elif len(unsatisfied_nodes) == 0:
        return G, labels_dict, 2

    G, labels_dict = shift_unsatisfied_node(G, labels_dict, rn.choice(unsatisfied_nodes), rn.choice(empty_cells))

    return G, labels_dict, 1


def rearrange_unsatisfied_nodes(G, labels_dict):

    steps_taken = 0

    while steps_taken <= 1000:
        G, labels_dict, this_step = rearrange_a_unsatisfied_node(G, labels_dict)

        if this_step == 0:
            print("No empty cells left")
            return G, labels_dict, 100000
        elif this_step == 1:
            steps_taken += 1
        else:
            print("All nodes are satisfied")
            break

    return G, labels_dict, steps_taken


N = 10

G, pos_dict, labels_dict = get_2D_graph(N)
# plot_2D_graph(G, pos_dict, labels_dict)

G = connect_diagonals_2D_graph(G, N)
# plot_2D_graph(G, pos_dict, labels_dict)

G = assign_type(G)
plot_2D_graph_colors(G, pos_dict, labels_dict)

G, labels_dict, steps_taken = rearrange_unsatisfied_nodes(G, labels_dict)
plot_2D_graph_colors(G, pos_dict, labels_dict)
print(steps_taken, "steps are taken.")
