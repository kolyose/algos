from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T):
        self._value: T = value
        self._prev: Optional[Node] = None

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value

    @property
    def prev(self) -> Optional["Node"]:
        return self._prev

    @prev.setter
    def prev(self, node: Optional["Node"]):
        self._prev = node


class Stack(Generic[T]):
    def __init__(self):
        self._last: Optional[Node] = None
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    @property
    def peek(self) -> T:
        if self._last is None:
            raise IndexError("peek() from an empty stack.")

        return self._last.value

    def append(self, value: T) -> "Stack":
        node = Node(value)
        if self._last is not None:
            node.prev = self._last
        self._last = node
        self._length += 1
        return self

    def pop(self) -> T:
        if self._last is None:
            raise IndexError("pop() from an empty stack.")

        node: Node = self._last
        self._last = node.prev
        self._length -= 1
        return node.value
