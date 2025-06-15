import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True

degree_centrality = nx.degree_centrality(G)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
closeness_centrality = nx.closeness_centrality(G)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
betweenness_centrality = nx.betweenness_centrality(G)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}
print(f"Number of nodes: {num_nodes}")  # Number of nodes: 4
print(f"Number of edges: {num_edges}")  # Number of edges: 4

path = nx.shortest_path(G, source="A", target="D")  # ['A', 'B', 'D']
avg_path_length = nx.average_shortest_path_length(G)  # 1.3333333333333333
print(f"Shortest path from A to D: {path}")  # Shortest path from A to D: ['A', 'B', 'D']

nx.draw(G, with_labels=True)
plt.show()

DG = nx.complete_graph(8)
options = {
    "node_color": "red",
    "edge_color": "green",
    "node_size": 500,
    "width": 3,
    "with_labels": True,
    "pos": nx.random_layout(DG)  # Use spring layout for better visualization
}
nx.draw(DG, **options)
plt.show()
