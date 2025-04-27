from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, priority: float):
        self._value = value
        self._priority = priority

    def __repr__(self) -> str:
        return f"<PriorityQueueNode value: {self._value} priority: {self._priority}>"

    @property
    def value(self) -> T:
        return self._value

    @property
    def priority(self) -> float:
        return self._priority


class PriorityQueue(Generic[T]):
    def __init__(self):
        self._nodes: list[Node[T]] = []

    def __len__(self) -> int:
        return len(self._nodes)

    def __repr__(self) -> str:
        return str(self._nodes)

    def __str__(self) -> str:
        return str(list(map(lambda node: node.priority, self._nodes)))

    def enqueue(self, value: T, priority: int):
        node = Node(value, priority)
        self._nodes.append(node)
        child_index = len(self._nodes) - 1
        parent_index = self._get_parent_index(child_index)

        while (
            parent_index is not None and self._nodes[parent_index].priority < priority
        ):
            self._nodes[parent_index], self._nodes[child_index] = (
                self._nodes[child_index],
                self._nodes[parent_index],
            )
            child_index = parent_index
            parent_index = self._get_parent_index(parent_index)

    def dequeue(self) -> Optional[T]:
        length = len(self._nodes)
        if length == 0:
            return None
        elif length == 1:
            node = self._nodes.pop()
            return node.value

        self._swap_values(0, length - 1)
        root = self._nodes.pop()

        parent_index = 0
        parent, child_indexes, children = self._get_parent_children_by_index(
            parent_index
        )

        while (
            children[0].priority > parent.priority
            or children[1].priority > parent.priority
        ):
            child_index = child_indexes[0]
            if children[0].priority < children[1].priority:
                child_index = child_indexes[1]
            self._swap_values(parent_index, child_index)

            parent_index = child_index
            parent, child_indexes, children = self._get_parent_children_by_index(
                parent_index
            )

        return root.value

    def _get_parent_index(self, index: int) -> Optional[int]:
        parent_index = (index - 1) // 2
        return parent_index if parent_index >= 0 else None

    def _get_parent_children_by_index(
        self, parent_index: int
    ) -> tuple[Node, list[int], list[Node]]:
        parent = self._nodes[parent_index]
        children_indexes = [(parent_index * 2) + 1, (parent_index * 2) + 2]
        children = list(
            map(
                lambda index: self._nodes[index]
                if index < len(self._nodes)
                else Node(None, float("-inf")),
                children_indexes,
            )
        )
        return (parent, children_indexes, children)

    def _swap_values(self, index1: int, index2: int):
        self._nodes[index1], self._nodes[index2] = (
            self._nodes[index2],
            self._nodes[index1],
        )
