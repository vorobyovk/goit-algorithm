import networkx as nx

# Функція для побудови Мінімального Остовного Дерева за алгоритмом Краскала
def kruskal_mst(graph):
    # Створюємо ліс, кожне дерево якого є окремою вершиною графа
    forest = nx.Graph()
    for node in graph.nodes():
        forest.add_node(node)

    # Сортування ребер графа за вагою в порядку зростання
    sorted_edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1))

    # Мінімальне остовне дерево
    mst = nx.Graph()

    # Додаємо ребра до МОД з урахуванням того, що додавання ребра не формує циклу
    for edge in sorted_edges:
        u, v, weight  = edge
        # Якщо u та v знаходяться в різних компонентах зв'язності, додаємо ребро
        if not nx.has_path(forest, u, v):
            forest.add_edge(u, v)
            mst.add_edge(u, v, weight=weight['weight'])

    return mst

# Створення зваженого графа
G = nx.Graph()
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'D', weight=5)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'D', weight=9)
G.add_edge('B', 'E', weight=7)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=15)
G.add_edge('D', 'F', weight=6)
G.add_edge('E', 'F', weight=8)
G.add_edge('E', 'G', weight=9)
G.add_edge('F', 'G', weight=11)

# Побудова мінімального остовного дерева за допомогою алгоритму Краскала
mst = kruskal_mst(G)

# Вивід ребер МОД
print("Edges in the MST:")
for edge in mst.edges(data=True):
    print(edge)
