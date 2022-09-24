import networkx as nx

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


def main():
    G = nx.erdos_renyi_graph(10, 0.5)
    G = set_all_A(G)

    listB = [0, 1]
    G = set_selected_B(G, listB)

    print_graph(G)


main()
