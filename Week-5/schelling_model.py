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
    empty_cells_list = []
    type1_node_list = []
    type2_node_list = []

    for cell in G.nodes():
        cell_type = rn.randint(0, 2)
        G._node[cell]['type'] = cell_type

        if cell_type == 0:
            empty_cells_list.append(cell)
        elif cell_type == 1:
            type1_node_list.append(cell)
        else:
            type2_node_list.append(cell)

    return G, empty_cells_list, type1_node_list, type2_node_list


N = 10

G, pos_dict, labels_dict = get_2D_graph(N)
# plot_2D_graph(G, pos_dict, labels_dict)

connect_diagonals_2D_graph(G, N)
# plot_2D_graph(G, pos_dict, labels_dict)

assign_type(G)
plot_2D_graph_colors(G, pos_dict, labels_dict)
