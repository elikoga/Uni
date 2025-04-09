"""
𝑆1
𝑆2
𝑆3
𝑆4
𝑆5
𝑆6
𝑇𝑠
ℎ
𝑇4
𝑑
𝑇4
𝑢
𝑇5
𝑑
𝑇5
𝑢
"""

class Node:
    def __init__(self, value, point, left=None, right=None):
        self.value = value
        self.point = point
        self.left = left
        self.right = right

    def largest_value(self):
        if self.right is None:
            return self.value
        return self.right.largest_value()

def build_tree(points):
    # sort points by x-coordinate, then y-coordinate
    points = sorted(points)
    # first, build lowest level of tree
    layer = []
    for point in points:
        layer.append(Node(point[0], None, None, None))
    # now, build tree from bottom up
    while len(layer) > 1:
        new_layer = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i+1] if i+1 < len(layer) else None
            new_node = Node(left.largest_value(), None, left, right)
            new_layer.append(new_node)
        layer = new_layer
    assert len(layer) == 1
    root = layer[0]
    # now, fill the tree
    points = sorted(points, key=lambda x: x[1])
    for point in points:
        node = root
        while node.point is not None:
            if point[0] <= node.value:
                assert node.left is not None
                node = node.left
            else:
                assert node.right is not None, f'{point} {node.point} {print_tree_graphviz(root)}'
                node = node.right
        node.point = point
    return root


def print_tree_graphviz(node, depth=0):
    all_nodes = []
    stack = [(node, depth)]
    while stack:
        node, depth = stack.pop()
        all_nodes.append(node)
        if node.left is not None:
            stack.append((node.left, depth+1))
        if node.right is not None:
            stack.append((node.right, depth+1))
    def node_name(node):
        # gives number of node in all_nodes
        return all_nodes.index(node)
    def label(node):
        if node.point:
          return f'{node.point}\\n{node.value}'
        return f'\\n{node.value}'
    print('digraph G {')
    for node in all_nodes:
        if node.left is not None:
            print(f'  {node_name(node)} -> {node_name(node.left)} [label="l"]')
        if node.right is not None:
            print(f'  {node_name(node)} -> {node_name(node.right)} [label="r"]')
        print(f'  {node_name(node)} [label="{label(node)}"]')
    print('}')


# Aufgabe 12 (5 Punkte):
# Given the point set
# P := (1, 1), (2, 8), (3, −5), (4, 9), (5, 11), (6, 3), (7, 4), (8, −6), (9, −1), (10, 4), (11, 7).
# (a) Draw the corresponding priority searchtree.
# (b) Execute the range query q = [2.5, 6.5] × (−∞, 10] (Mark visited edges/nodes and the output.).

points = [(1, 1), (2, 8), (3, -5), (4, 9), (5, 11), (6, 3), (7, 4), (8, -6), (9, -1), (10, 4), (11, 7)]

root = build_tree(points)

# print_tree_graphviz(root)

q = ((2.5, 6.5), (-float('inf'), 10))

def range_query(node, q):
    visited_edges = []
    visited_nodes = []

    out = []

    stack = [node]

    while stack:
        node = stack.pop()
        visited_nodes.append(node)
        # check left child
        if node.left is not None:
            # check if range intersects with node
            if q[0][0] <= node.value and node.left.point is not None and q[1][1] >= node.left.point[1]:
                visited_edges.append((node, node.left))
                stack.append(node.left)
        # check right child
        if node.right is not None:
            # check if range intersects with node
            if q[0][1] > node.value and node.right.point is not None and q[1][1] >= node.right.point[1]:
                visited_edges.append((node, node.right))
                stack.append(node.right)

        if node.point is not None and q[0][0] <= node.point[0] <= q[0][1] and q[1][0] <= node.point[1] <= q[1][1]:
            out.append(node.point)
    return visited_edges, visited_nodes, out

def print_with_query(node, q):
    visited_edges, visited_nodes, out = range_query(node, q)
    all_nodes = []
    stack = [node]
    while stack:
        node = stack.pop()
        all_nodes.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    def node_name(node):
        return all_nodes.index(node)
    def label(node):
        if node.point:
          return f'{node.point}\\n{node.value}'
        return f'\\n{node.value}'
    print('digraph G {')
    for node in all_nodes:
        if node.left is not None:
            if (node, node.left) in visited_edges:
                print(f'  {node_name(node)} -> {node_name(node.left)} [label="l", color=red]')
            else:
                print(f'  {node_name(node)} -> {node_name(node.left)} [label="l"]')
        if node.right is not None:
            if (node, node.right) in visited_edges:
                print(f'  {node_name(node)} -> {node_name(node.right)} [label="r", color=red]')
            else:
                print(f'  {node_name(node)} -> {node_name(node.right)} [label="r"]')
        if node in visited_nodes:
            print(f'  {node_name(node)} [label="{label(node)}", color=red]')
        else:
            print(f'  {node_name(node)} [label="{label(node)}"]')
    print('}')

print_with_query(root, q)

print(f"Output: {range_query(root, q)[2]}")