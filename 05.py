import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import color_gradient_05


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph, pos


def draw_tree(tree, pos, visited_list):
    color1 = "#013812"
    color2 = "#4fc975"
    colors_gradients = color_gradient_05.get_color_gradient(color1, color2, len(visited_list))

    for i, node_id in enumerate(visited_list):
        for node in tree.nodes(data=True):
            if node[0] == node_id:
                node[1]['color'] = colors_gradients[i]
                break

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_recursive(root, tree, vertex=None, visited=None, visited_list=None):

    if vertex is None:
        vertex = root.id

    if visited is None and visited_list is None:
        visited = set()
        visited_list = list()

    visited.add(vertex)
    visited_list.append(vertex)
    for neighbor in tree[vertex]:
        if neighbor not in visited:
            dfs_recursive(root, tree, neighbor, visited, visited_list)
    
    return visited_list


def bfs_recursive(tree, queue=None, visited=None, visited_list=None):
    if visited is None and visited_list is None:
        visited = set()
        visited_list = list()

    if queue is None:
        queue = deque([root.id])
    elif not queue:
        return

    vertex = queue.popleft()

    if vertex not in visited:
        visited_list.append(vertex)
        visited.add(vertex)
        queue.extend(set(tree[vertex]) - visited)

    bfs_recursive(tree, queue, visited, visited_list)

    return visited_list


def draw_dfs_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree, pos = add_edges(tree, root, pos)
    visited_list = dfs_recursive(root, tree)
    draw_tree(tree, pos, visited_list)
    

def draw_bfs_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree, pos = add_edges(tree, root, pos)
    visited_list = bfs_recursive(tree)
    draw_tree(tree, pos, visited_list)


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(6)


draw_dfs_tree(root)
draw_bfs_tree(root)
