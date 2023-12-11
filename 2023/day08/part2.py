from math import lcm

class Node:

    def __init__(self, name):
        self.name: str = name
        self.children: list = []

    def get_child(self, index: int):
        return self.children[index]
    
    def add_children(self, child):
        self.children.extend(child)

    def __str__(self) -> str:
        return f"{self.name} = ({self.children[0].name}, {self.children[1].name})"

def main():
    f = open("input2.txt", "r")
    lines: list[str] = f.readlines()
    f.close()

    sequence: list[int] = list(map(lambda x: 0 if x == 'L' else 1, lines[0][0:-1]))
    node_map: dict[str, Node] = {}
    for line in lines[2:]:
        tokens = line.split(" = ")
        children = tokens[1][1:-2].split(", ")
        children_nodes = []
        for child in children:
            if child in list(node_map.keys()):
                children_nodes.append(node_map[child])
            else:
                node = Node(child)
                children_nodes.append(node)
                node_map[child] = node

        if tokens[0] in list(node_map.keys()):
            node_map[tokens[0]].add_children(children_nodes)
        else:
            node = Node(tokens[0])
            node.add_children(children_nodes)
            node_map[tokens[0]] = node


    nodes: list[Node] = list(map(lambda x: node_map[x],filter(lambda x: x.endswith('A'),node_map.keys())))

    res: list[int] = []
    for n in nodes:
        steps: int = 0
        v = 0
        while v == 0:
            if n.name.endswith("Z"):
                v = steps
            n = n.get_child(sequence[steps%len(sequence)])
            steps += 1
        res.append(v)

    print(res)
    print(lcm(*res))

    

if __name__ == "__main__":
    main()

#18625484023687