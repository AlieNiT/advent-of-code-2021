class Node:
    def __init__(self, name: str):
        self.name = name
        self.small = name.islower()
        self.neighbors = []

    def add_neighbor(self, node):
        if node in self.neighbors:
            return
        self.neighbors.append(node)

    def explore(self, path, end):
        if self == end:
            return 1
        res = 0
        next_path = path.copy()
        if self.name != "start":
            next_path.append(self)
        for neighbor in self.neighbors:
            if neighbor in path and neighbor.small:
                continue
            res += neighbor.explore(next_path, end)
        return res


nodes = {}
while True:
    inp = input()
    if inp == "end":
        break
    edge_nodes = inp.split("-")
    for node_name in edge_nodes:
        if not (node_name in nodes.keys()):
            nodes[node_name] = Node(node_name)
    nodes[edge_nodes[0]].add_neighbor(nodes[edge_nodes[1]])
    nodes[edge_nodes[1]].add_neighbor(nodes[edge_nodes[0]])
print(nodes["start"].explore([nodes["start"]], nodes["end"]))
