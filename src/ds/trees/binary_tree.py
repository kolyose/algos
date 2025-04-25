from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T):
        self._value = value
        self._left: Optional[Node] = None
        self._right: Optional[Node] = None

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value

    @property
    def left(self) -> Optional["Node"]:
        return self._left

    @left.setter
    def left(self, node: "Node"):
        self._left = node

    @property
    def right(self) -> Optional["Node"]:
        return self._right

    @right.setter
    def right(self, node: "Node"):
        self._right = node

    def __repr__(self) -> str:
        return str(self._value)


class BinaryTree(Generic[T]):
    def __init__(self):
        self._root: Optional[Node[T]] = None

    @property
    def root(self) -> Optional["Node[T]"]:
        return self._root

    def print(self):
        if self.root is None:
            return ""

        levels = [[self.root]]

        def compose_next_level(nodes: list[Node[T]]):
            level = []
            for node in nodes:
                if node:
                    level.append(node.left)
                    level.append(node.right)
                else:
                    level.append(None)

            if all(node is None for node in level):
                return

            levels.append(level)
            compose_next_level(level)

        compose_next_level(levels[0])

        def convert_to_2digit(value: str) -> str:
            return value if len(value) > 1 else f"0{value}"

        length = len(levels)
        for index, values in enumerate(levels):
            outer_delimiter = f"{' ' * (length - index) * 4}"
            inner_delimiter = f"{' ' * (length - index) * 3}"
            level = ""
            for i in range(len(values)):
                if i % 2 == 0:
                    level += outer_delimiter
                    level += (
                        convert_to_2digit(str(values[i].value))
                        if values[i] is not None
                        else "  "
                    )
                else:
                    level += inner_delimiter
                    level += (
                        convert_to_2digit(str(values[i].value))
                        if values[i] is not None
                        else "  "
                    )
            level += "\n"
            if index < len(levels) - 1:
                for i in range(len(values)):
                    if i % 2 == 0:
                        level += outer_delimiter[0:-1]
                        level += "/  \\" if values[i] is not None else "  "
                    else:
                        level += inner_delimiter[0:-1]
                        level += "/  \\" if values[i] is not None else "  "

            print(level)
