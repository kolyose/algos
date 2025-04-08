from typing import Optional, Iterator, Iterable


class Node:
    """
    A class representing a node in a doubly linked list.

    Methods:
        value (object): Gets or sets the value of the node.
        next (Optional[Node]): Gets or sets the reference to the next node in the list.
        prev (Optional[Node]): Gets or sets the reference to the previous node in the list.
    """

    def __init__(self, value: object):
        self._value: object = value
        self._next: Optional[Node] = None
        self._prev: Optional[Node] = None

    @property
    def value(self) -> object:
        return self._value

    @value.setter
    def value(self, value: object):
        self._value = value

    @property
    def prev(self) -> Optional["Node"]:
        return self._prev

    @prev.setter
    def prev(self, node: Optional["Node"]):
        self._prev = node

    @property
    def next(self) -> Optional["Node"]:
        return self._next

    @next.setter
    def next(self, node: Optional["Node"]):
        self._next = node

    def __repr__(self) -> str:
        return f"<Node value: {self.value}>"

    def __str__(self) -> str:
        return str(self.value)


# TODO: extract common methods in a base class?
class DoublyLinkedList:
    """
    A class representing a Doubly Linked List.

    Methods
    -------
    __init__(init_list: Optional[Iterable[object]] = None)
        Initializes the linked list. Optionally takes an iterable to populate the list.
    __iter__() -> Iterator[object]
        Returns an iterator for the linked list.
    __len__() -> int
        Returns the number of nodes in the linked list.
    __getitem__(index: int) -> object
        Returns the value of the node at the specified index.
    __setitem__(index: int, value: object) -> None
        Sets the value of the node at the specified index.
    __delitem__(index: int) -> None
        Deletes the node at the specified index.
    __contains__(value: object) -> bool
        Checks if a value is present in the linked list.
    __add__(addition: list | DoublyLinkedList) -> DoublyLinkedList
        Concatenates a list or another DoublyLinkedList to the current list.
    __mul__(multiplier: int) -> DoublyLinkedList
        Repeats the linked list a specified number of times.
    __repr__() -> str
        Returns a string representation of the linked list.
    __str__() -> str
        Returns a string representation of the values in the linked list.
    head() -> Node
        Returns the head node of the linked list.
    tail() -> Node
        Returns the tail node of the linked list.
    append(value: object) -> DoublyLinkedList
        Appends a value to the end of the linked list.
    pop(index: Optional[int] = None) -> Node
        Removes and returns the node at the specified index.
    insert(index: int, value: object) -> DoublyLinkedList
        Inserts a value at the specified index.
    remove(value: object) -> DoublyLinkedList
        Removes the first occurrence of a value in the linked list.
    extend(addition: "list | DoublyLinkedList") -> DoublyLinkedList
        Extends the linked list by appending elements from another list or DoublyLinkedList.
    copy() -> DoublyLinkedList
        Returns a shallow copy of the linked list.
    clear() -> DoublyLinkedList
        Clears the linked list.
    """

    def __init__(self, init_list: Optional[Iterable[object]] = None):
        """
        Initialize a doubly linked list. Optionally, populates the list with
        elements from an iterable.

        Args:
            init_list (Optional[Iterable[object]]): An optional iterable of
                elements to initialize the linked list with. If None, an empty
                list is created.

        Raises:
            TypeError: If the provided `init_list` is not an iterable.
        """
        self._init()
        if init_list is not None:
            try:
                for value in init_list:
                    self.append(value)
            except TypeError:
                raise TypeError(f"{type(init_list)} object is not iterable")

    def __iter__(self) -> Iterator[object]:
        """
        Iterate over the elements of the doubly linked list.

        Returns:
            Iterator[object]: An iterator, that yealds the value of each node in the doubly linked list,
            starting from the head and proceeding to the tail.
        """
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __reversed__(self) -> Iterator[object]:
        """
        Iterate over the elements of the doubly linked list in reverse order.

        Returns:
            Iterator[object]: An iterator, that yealds the value of each node in the doubly linked list,
            starting from the tail and proceeding to the head.
        """
        current_node = self.tail
        while current_node is not None:
            yield current_node.value
            current_node = current_node.prev

    def __len__(self) -> int:
        """
        Return the number of elements in the doubly linked list.

        Returns:
            int: The number of elements in the list.
        """
        return self._length

    def __getitem__(self, index: int) -> object:
        """
        Retrieve the value of the node at the specified index in the doubly linked list.

        Args:
            index (int): The index of the node to retrieve. Can be negative to indicate
                         indexing from the end of the list.

        Returns:
            object: The value of the node at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
            AssertionError: If the tail node is None when accessing the last element.

        Notes:
            - Negative indexing is supported, where -1 refers to the last element,
              -2 refers to the second-to-last element, and so on.
            - Relies on internal method _get_note_at(index), which iterates forwards
              from the head if the specified index is less than half of the list,
              and backwards from the tail otherwise - for performance reasons.
        """
        return self._get_node_at(index).value

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value of the node at the specified index in the doubly linked list.

        Args:
            index (int): The zero-based index of the node to update.
            value (object): The new value to assign to the node.

        Raises:
            IndexError: If the index is out of the bounds of the list.
        """
        node: Node = self._get_node_at(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """
        Remove the item at the specified index from the doubly linked list.

        This method is called when the `del` statement is used on an instance
        of the doubly linked list with a specific index. Internally, it uses
        the `pop` method to remove the item.

        Args:
            index (int): The zero-based index of the item to be removed.

        Raises:
            IndexError: If the index is out of range.
        """
        self.pop(index)

    def __contains__(self, value: object) -> bool:
        """
        Check if a value is present in the doubly linked list.

        This method is called when the `in` statement is used on an instance
        of the doubly linked list with a specific value.

        Args:
            value (object): The value to search for in the list.

        Returns:
            bool: True if the value is found in the list, False otherwise.
        """
        if self._length == 0:
            return False

        for val in self:
            if value == val:
                return True
        return False

    def __add__(self, addition: "list | DoublyLinkedList") -> "DoublyLinkedList":
        """
        Implement the concatenation '+' operator.

        Args:
            addition (list | DoublyLinkedList): The list or DoublyLinkedList to concatenate
                to the current DoublyLinkedList.

        Returns:
            DoublyLinkedList: A new DoublyLinkedList instance containing the elements
                of the current list followed by the elements of the provided `addition`.

        Raises:
            TypeError: If `addition` is not a list or a DoublyLinkedList.
        """
        if not isinstance(addition, list) and not isinstance(
            addition, DoublyLinkedList
        ):
            raise TypeError(
                f"can only concatenate list or DoublyLinkedList (not {type(addition)}) to DoublyLinkedList"
            )
        copy = self.copy()
        for value in addition:
            copy.append(value)
        return copy

    def __mul__(self, multiplier: int) -> "DoublyLinkedList":
        """
        Implement the multiplication '*' operator.

        This method allows a doubly linked list to be multiplied by an integer,
        effectively repeating the list's elements the specified number of times.

        Args:
            multiplier (int): The number of times to repeat the list. Must be a non-negative integer.

        Returns:
            DoublyLinkedList: A new doubly linked list containing the repeated elements.

        Raises:
            TypeError: If the multiplier is not an integer.

        Notes:
            - If the multiplier is less than 1 (including 0 or False), the resulting list will be empty.
            - The method creates a copy of the original list and does not modify it.
        """
        if not isinstance(multiplier, int):
            raise TypeError(
                f"can't multiply sequence by non-int of type {type(multiplier)}"
            )
        copy = self.copy()
        res = copy
        if multiplier < 1 or multiplier is False:
            res.clear()
        else:
            for _ in range(multiplier - 1):
                res += copy
        return res

    def __repr__(self) -> str:
        """
        Provide a string representation of the DoublyLinkedList instance.

        Returns:
            str: A string describing the DoublyLinkedList, including its values.
        """
        return f"<DoublyLinkedList values: {str(self)}>"

    def __str__(self) -> str:
        """
        Provide a string representation of the doubly linked list values.

        Returns:
            str: A string representation of a python list composed of values in the linked list.
        """
        lst: list = []
        for value in self:
            lst.append(value)
        return str(lst)

    @property
    def head(self) -> Optional[Node]:
        """
        Retrieve the head node of the doubly linked list.

        Returns:
            Optional[Node]: The head node of the list if it exists, otherwise None.
        """
        return self._head

    @property
    def tail(self) -> Optional[Node]:
        """
        Retrieve the tail node of the doubly linked list.

        Returns:
            Optional[Node]: The tail node of the list if it exists, otherwise None.
        """
        return self._tail

    def append(self, value: object) -> "DoublyLinkedList":
        """
        Append a new node with the given value to the end of the doubly linked list.

        Args:
            value (object): The value to be stored in the new node.

        Returns:
            DoublyLinkedList: The instance of the doubly linked list to allow method chaining.
        """
        node = Node(value)
        if self._head is None:
            self._head = node
        if self._tail is not None:
            node.prev = self._tail
            self._tail.next = node
        self._tail = node
        self._length += 1

        return self

    def pop(self, index: Optional[int] = None) -> object:
        """
        Remove the node at the specified index in the doubly linked list.
        If no index is provided, remove the last node.

        Args:
            index (Optional[int]): The index of the node to remove. Defaults to None,
                                   which removes the last node.

        Returns:
            object: The value of the removed node.

        Raises:
            AssertionError: If the list is empty (head is None) or if a non-tail node
                            references None.
            IndexError: If the provided index is out of bounds.
        """
        if index is None:
            index = self._length - 1
        else:
            self._validate_index(index)

        assert self._head is not None, "The non-empty list's Head node is None."
        node: Node = self._head

        if self._length == 1:
            self._head = None
            self._tail = None
        elif index == 0:
            assert self._head.next is not None, "A non-tail node is referencing None."
            self._head.next.prev = None
            self._head = self._head.next
        elif index == self._length - 1:
            assert self._tail is not None, "The non-empty list's Tail node is None."
            node = self._tail
            assert node.prev is not None, "A non-head node is referencing None."
            node.prev.next = None
            self._tail = node.prev
        else:
            node: Node = self._get_node_at(index)
            assert node.prev is not None, "A non-head node is referencing None"
            node.prev.next = node.next
            assert node.next is not None, "A non-tail node is referencing None"
            node.next.prev = node.prev

        self._length -= 1
        return node.value

    def insert(self, index: int, value: object) -> "DoublyLinkedList":
        """
        Insert a new value at the specified index in the doubly linked list.

        Args:
            index (int): The position at which to insert the new value.
                         Can be negative to indicate positions from the end of the list.
            value (object): The value to insert into the list.

        Returns:
            DoublyLinkedList: The updated doubly linked list instance.

        Raises:
            TypeError: If the provided index is not an integer.
            IndexError: If the absolute value of the index is greater than the length of the list.

        Notes:
            - If the index is equal to the length of the list, the value is appended to the end.
            - If the index is 0, the value is inserted at the head of the list.
        """
        if type(index) is not int:
            raise TypeError(f"Index {index} is not of int type.")

        if abs(index) > self._length:
            raise IndexError(f"Index {index} is out of the list boundaries.")

        if index < 0:
            index = self._length + index

        node = Node(value)
        if self._length == 0:
            self._head = node
            self._tail = node
        elif index == 0:
            assert self._head is not None, "The non-empty list's Head node is None."
            node.next = self._head
            node.next.prev = node
            self._head = node
        elif index == self._length:
            return self.append(value)
        else:
            node_at_index = self._get_node_at(index)
            node.prev = node_at_index.prev
            if node.prev:
                node.prev.next = node
            node.next = node_at_index
            node.next.prev = node

        self._length += 1
        return self

    def remove(self, value: object) -> "DoublyLinkedList":
        """
        Remove the first occurrence of the specified value from the doubly linked list.

        If the value is found at the head or tail of the list, it is removed directly.
        Otherwise, the method traverses the list to find and remove the value.

        Args:
            value (object): The value to be removed from the list.

        Returns:
            DoublyLinkedList: The updated doubly linked list after the removal.

        Raises:
            ValueError: If the specified value is not found in the list.
        """
        if self.head and self.head.value == value:
            self.pop(0)
            return self

        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                self._length -= 1
                return self

            current_node = current_node.next

        raise ValueError(f"{value} is not in list")

    def extend(self, addition: "list | DoublyLinkedList") -> "DoublyLinkedList":
        """
        Extend the current doubly linked list by appending elements from another list
        or another DoublyLinkedList.

        Args:
            addition (list | DoublyLinkedList): The collection of elements to append.
                It can be either a Python list or another DoublyLinkedList.

        Returns:
            DoublyLinkedList: The updated doubly linked list after appending the elements.

        Raises:
            TypeError: If the `addition` argument is not a list or a DoublyLinkedList.
        """
        if not isinstance(addition, list) and not isinstance(
            addition, DoublyLinkedList
        ):
            raise TypeError(
                f"can extend DoublyLinkedList only with list or DoublyLinkedList (not {type(addition)})"
            )
        for value in addition:
            self.append(value)
        return self

    def copy(self) -> "DoublyLinkedList":
        """
        Create a shallow copy of the doubly linked list.

        Returns:
            DoublyLinkedList: A new doubly linked list containing the same elements
            as the original list, in the same order.
        """
        new_list = DoublyLinkedList()
        for value in self:
            new_list.append(value)
        return new_list

    def clear(self) -> "DoublyLinkedList":
        """
        Clears the doubly linked list by reinitializing it to an empty state.

        Returns:
            DoublyLinkedList: The current instance of the doubly linked list after being cleared.
        """
        self._init()
        return self

    def _init(self) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._length: int = 0

    def _validate_index(self, index: int) -> bool:
        if type(index) is not int:
            raise TypeError(f"Index {index} is not of int type.")

        if index < 0:
            if abs(index) > self._length:
                raise IndexError(f"Index {index} is out of the list boundaries.")
        else:
            if index >= self._length:
                raise IndexError(f"Index {index} is out of the list boundaries.")

        return True

    def _get_node_at(self, index: int) -> Node:
        self._validate_index(index)

        if index < 0:
            index = self._length + index

        current_index = 0
        current_node: Node

        if index > self._length // 2:
            current_index = self._length - 1
            assert self.tail is not None, "The non-empty list's Tail node is None."
            current_node = self.tail
            while current_index != index:
                assert current_node.prev is not None, (
                    "A non-head node is referencing None."
                )
                current_node = current_node.prev
                current_index -= 1
        else:
            current_index = 0
            assert self.head is not None, "The non-empty list's Head node is None."
            current_node = self.head
            while current_index != index:
                assert current_node.next is not None, (
                    "A non-tail node is referencing None."
                )
                current_node = current_node.next
                current_index += 1

        return current_node
