from ds.trees.binary_tree import BinaryTree, Node
from ds.queue import Queue


def breadth_first(tree: BinaryTree) -> list:
    result = []
    if tree.root is None:
        return result

    queue = Queue(tree.root)
    while len(queue):
        node: Node = queue.dequeue()
        result.append(node.value)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return result


def depth_first_pre_order(tree: BinaryTree) -> list:
    result = []
    if tree.root is None:
        return result

    def traverse_node(node: Node):
        result.append(node.value)
        if node.left:
            traverse_node(node.left)
        if node.right:
            traverse_node(node.right)

    traverse_node(tree.root)
    return result


def depth_first_post_order(tree: BinaryTree) -> list:
    result = []
    if tree.root is None:
        return result

    def traverse_node(node: Node):
        if node.left:
            traverse_node(node.left)
        if node.right:
            traverse_node(node.right)
        result.append(node.value)

    traverse_node(tree.root)
    return result


def depth_first_in_order(tree: BinaryTree) -> list:
    result = []
    if tree.root is None:
        return result

    def traverse_node(node: Node):
        if node.left:
            traverse_node(node.left)

        result.append(node.value)

        if node.right:
            traverse_node(node.right)

    traverse_node(tree.root)
    return result
