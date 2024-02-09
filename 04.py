import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


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
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap):
    root = Node(heap[0])
    nodes = [root]

    for i, _ in enumerate(heap):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        current_node = nodes.pop(0)       

        if left_index > (len(heap)-1):
            break
        else:
            left_value = heap[left_index]
            current_node.left = Node(left_value)     
            nodes.append(current_node.left)       

        if right_index > (len(heap)-1):
            break
        else:
            right_value = heap[right_index]
            current_node.right = Node(right_value)  
            nodes.append(current_node.right)
                          
    return root


def draw_heap(heap):
    heapq.heapify(arr)
    heap_tree = heap_to_tree(heap)
    draw_tree(heap_tree)


arr = [5, 1, 4, 3, 2, 7, 56, 8, 65, 9, 0, 6, 77, 88, 99, 101]
draw_heap(arr)
