from audioop import reverse
import networkx as nx
import random as rn
import numpy as np


def random_walk(G, mul):
    nodes = list(G.nodes())

    focus = rn.choice(nodes)

    counter = 0
    limit = mul * G.order()

    while(counter < limit):

        next = rn.choice(nodes)

        if focus !=next and G.has_edge(focus, next) == 0:
            G.add_edge(focus, next)

        focus = next

        counter += 1
    
    return G

def isComplete(G):
    nodes = G.nodes()

    for i in nodes:
        for j in nodes:
            if i!=j and (G.has_edge(i, j)==0  or G.has_edge(j, i)==0):
                return False
    
    return True


def main():
    G = nx.DiGraph()

    n = 20

    for i in range(n):
        G.add_node(i)

    G = random_walk(G, 5000)

    print(nx.is_strongly_connected(G))
    print(isComplete(G))


main()