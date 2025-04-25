from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    """
    A class representing a node in a queue.

    Methods:
        value (object): Gets or sets the value of the node.
        next (Optional[Node]): Gets or sets the reference to the next node in the queue.
    """

    def __init__(self, value: T):
        self._value: T = value
        self._next: Optional[Node] = None

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value

    @property
    def next(self) -> Optional["Node"]:
        return self._next

    @next.setter
    def next(self, node: Optional["Node"]):
        self._next = node


class Queue(Generic[T]):
    def __init__(self, value: T):
        self._first: Optional[Node] = None
        self._last: Optional[Node] = None
        self._length: int = 0

        if value is not None:
            self.enqueue(value)

    def __len__(self) -> int:
        return self._length

    @property
    def peek(self) -> T:
        if self._first is None:
            raise IndexError("peek() from an empty queue.")

        return self._first.value

    def enqueue(self, value: T) -> "Queue":
        node = Node(value)
        if self._first is None:
            self._first = node
        if self._last is not None:
            self._last.next = node
        self._last = node
        self._length += 1
        return self

    def dequeue(self) -> T:
        if self._first is None:
            raise IndexError("dequeue() from an empty queue.")

        node: Node = self._first
        self._first = node.next
        self._length -= 1
        if self._length == 0:
            self._last = None
        return node.value
