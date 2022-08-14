import networkx as nx
import itertools as it


def communities_brute(G):
    nodes = G.nodes()
    n = G.order()
    e = G.size()

    first_community = []
    second_community = []

    for i in range(1, 1 + int(n/2)):
        comb1 = []
        comb2 = []

        for x in it.combinations(nodes, i):
            listX = list(x)
            comb1.append(listX)
            comb2.append(list(set(nodes) - set(x)))

        first_community.extend(comb1)
        second_community.extend(comb2)

    maxRatio = 0.0
    maxIndex = -1

    for i in range(len(first_community)):
        sG1 = G.subgraph(first_community[i])
        interEdges1 = sG1.size()

        sG2 = G.subgraph(second_community[i])
        interEdges2 = sG2.size()

        intraEdges = e - interEdges1 - interEdges2

        thisRatio = float(interEdges1 + interEdges2)/intraEdges

        if thisRatio >= maxRatio:
            maxRatio = thisRatio
            maxIndex = i

    print("Community 1 is: ", first_community[maxIndex])
    print("Community 2 is: ", second_community[maxIndex])


Gr = nx.barbell_graph(3, 0)
communities_brute(Gr)
