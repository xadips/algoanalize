import random
import collections
import networkx as nx
#from networkx.generators.random_graphs import erdos_renyi_graph
#import matplotlib.pyplot as plt
import time

print("Įveskite grafą G(V, E):")
V = eval(input("V = "))
E = eval(input("E = "))


# Atsitiktinio grafo generavimas
#G = erdos_renyi_graph(500, 0.35)
#V = G.nodes
#E = G.edges
#print("n = %s" % (len(G.nodes)))
# print(G.nodes)
#print("m = %s" % (len(G.edges)))
# print(G.edges)

# Testiniai duomenys
#V = [1, 2, 3, 4, 5]
#E = [(1, 2), (1, 3), (2, 3), (3, 4)]
# Output: [{1, 2, 3}, {3, 4}, {5}]


# Sudarome kaimynų aibę N, kur N(i), i-ojo elemento kaimynų sąrašas
N = collections.defaultdict(set)
for (src, dst) in E:
    N[src].add(dst)
    N[dst].add(src)


def generate_maximal_cliques(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    try:
        u = random.choice(list(P.union(X)))
        S = P.difference(N[u])
    # Jeigu sąjunga P ir X tuščia
    except IndexError:
        S = P
    for v in S:
        yield from generate_maximal_cliques(
            P=P.intersection(N[v]), R=R.union([v]), X=X.intersection(N[v]))
        P.remove(v)
        X.add(v)


start_time = time.time()
print(list(generate_maximal_cliques(V)))
# Kai tikriname tik generavimo ne išvedimo laiką vardan tikslumo
# list(generate_maximal_cliques(V))
elapsed_time = time.time() - start_time
print("Runtime: %s" % (elapsed_time))

# Grafo atvaizdavimas su atsitiktiniais grafais
#visual = []
# nx.draw_networkx(G)
# plt.show()
