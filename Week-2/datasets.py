import networkx as nx
import matplotlib.pyplot as plt


def plot_degree_dist(G):
    all_degrees = list(nx.degree(G))
    freq_count = {}
    mx = 0
    my = 0

    for degree in all_degrees:
        temp = freq_count.get(degree[1], 0) + 1
        freq_count[degree[1]] = temp
        mx = max(mx, degree[1])
        my = max(my, temp)

    lim = mx + 1

    x = []
    y = []

    for degree in range(lim):
        x.append(degree)
        y.append(freq_count.get(degree, 0))

    plt.xlabel('Degree')
    plt.ylabel('Number of Nodes')
    plt.title('Degree Distribution of Graph')
    plt.axis([0, mx, 0, my])
    plt.plot(x, y)
    plt.show()


G1 = nx.read_edgelist('Network Datasets/facebook_combined.txt')
G2 = nx.read_graphml('Network Datasets/airlines.graphml')
G3 = nx.read_gml('Network Datasets/karate.gml', label='id')
G4 = nx.read_pajek('Network Datasets/football.net')
# G5 = nx.read_gexf('Network Datasets/EuroSiS_Generale_Pays.gexf')

# plot_degree_dist(G1)
# plot_degree_dist(G2)
plot_degree_dist(G3)
# plot_degree_dist(G4)
