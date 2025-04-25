from typing import Optional
from ds.trees.binary_tree import Node, BinaryTree


class BinarySearchTree(BinaryTree[int]):
    def __init__(self):
        super().__init__()

    def insert(self, value: int) -> Optional[Node[int]]:
        node = Node(value)
        if self._root is None:
            self._root = node
            return node

        current_node: Node = self._root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = node
                    return node
                current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = node
                    return node
                current_node = current_node.right
            else:
                return None

    def find(self, value: int) -> Optional[Node[int]]:
        if self._root is None:
            return None

        current_node = self._root
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None
