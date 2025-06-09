import networkx as nx

#неориентированный граф
G = nx.Graph()
G.add_node("A")
G.add_nodes_from(["B", "C", "D"])
G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

print(list(G.neighbors("A")))  # ['B', 'C']
print(list(G.neighbors("D")))  # ['B', 'C']

G.remove_edge("A", "B")
G.remove_edges_from([("A", "C"), ("B", "D")])
G.remove_node("A")
G.remove_edge("C", "B")
print(f"NODES: {G.nodes}")  # ['B', 'C', 'D']
print(f"EDGES: {G.edges}")  # [('B', 'C'), ('B', 'D')]


#ориентированный граф
DG = nx.DiGraph()

DG.add_nodes_from(["A", "B", "C", "D"])

DG.add_edge("A", "B")
DG.add_edge("B", "A")
print(list(DG.neighbors("A")))  # ['B']
print(list(DG.neighbors("B")))  # ['A']
DG.add_edges_from([("D", "B"), ("B", "C")])
print(list(DG.successors("B")))  
neighbors_of_A = DG["A"]
print(f"neighbors_of_A: {neighbors_of_A}")
DG.nodes["A"]["color"] = "blue"
print(f"Color of A: {DG.nodes['A']['color']}")  # Color of A: blue
DG["A"]["B"]["weight"] = 5
print(f"Weight of edge A-B: {DG['A']['B']['weight']}")  # Weight of edge A-B: 5