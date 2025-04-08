import pytest
from contextlib import nullcontext
from src.ds.lists.doubly_linked_list import DoublyLinkedList


# TODO: extract common test methods in a base test class?
class TestDoublyLinkedList:
    def setup_method(self):
        self.initializer: list = [1, 2, 3]
        self.list = DoublyLinkedList(self.initializer)

    @pytest.mark.parametrize(
        "initializer,expectation",
        [
            (None, nullcontext(("[]", 0))),
            ([], nullcontext(("[]", 0))),
            ({}, nullcontext(("[]", 0))),
            ((), nullcontext(("[]", 0))),
            (set(), nullcontext(("[]", 0))),
            ("", nullcontext(("[]", 0))),
            (DoublyLinkedList(), nullcontext(("[]", 0))),
            ([1, 2, 3], nullcontext(("[1, 2, 3]", 3))),
            ({"a": 1, "b": 2, "c": 3}, nullcontext(("['a', 'b', 'c']", 3))),
            ((1, 2, 3), nullcontext(("[1, 2, 3]", 3))),
            ({1, 2, 3}, nullcontext(("[1, 2, 3]", 3))),
            ("123", nullcontext(("['1', '2', '3']", 3))),
            (1, pytest.raises(TypeError)),
        ],
    )
    def test_instantiation(self, initializer, expectation):
        with expectation as e:
            (string, length) = e
            self.list = DoublyLinkedList(initializer)
            assert isinstance(self.list, DoublyLinkedList)
            assert str(self.list) == string
            assert len(self.list) == length

    def test_consistency(self):
        lst = DoublyLinkedList([1, 2, 3, 4, 5])
        lst.append(6)
        lst.pop()
        lst.insert(1, 2)
        lst.insert(6, 6)
        lst += [7, 8, 9]
        lst.remove(2)

        assert str(lst) == "[1, 2, 3, 4, 5, 6, 7, 8, 9]"

        for i in range(len(lst) - 1):
            node = lst._get_node_at(i)
            next_node = lst._get_node_at(i + 1)
            assert lst[i] == i + 1
            assert node.next is next_node
            assert next_node.prev is node

    def test__iter__(self):
        for index, value in enumerate(self.list):
            assert value == self.initializer[index]

    def test__reversed__(self):
        length = len(self.list)
        for index, value in enumerate(reversed(self.list)):
            assert value == self.list[length - 1 - index]

    def test__len__(self):
        assert len(self.list) == 3

    def test__getitem__(self):
        for index in range(len(self.list)):
            assert self.list[index] == self.initializer[index]

    def test__setitem__(self):
        index = 0
        new_value = -1
        self.list[index] = new_value
        assert self.list[index] == new_value

    def test__delitem__(self):
        del self.list[1]
        assert len(self.list) == len(self.initializer) - 1
        assert self.list[0] == self.initializer[0]
        assert self.list[1] == self.initializer[2]

    def test__contains__(self):
        for value in self.initializer:
            assert value in self.list

        assert -1 not in self.list

    @pytest.mark.parametrize(
        "input, expectation",
        [
            ((DoublyLinkedList([]), []), nullcontext("[]")),
            ((DoublyLinkedList([]), DoublyLinkedList([])), nullcontext("[]")),
            ((DoublyLinkedList([1, 2, 3]), []), nullcontext("[1, 2, 3]")),
            (
                (DoublyLinkedList([1, 2, 3]), DoublyLinkedList([])),
                nullcontext("[1, 2, 3]"),
            ),
            (
                (DoublyLinkedList([1, 2, 3]), [4, 5, 6]),
                nullcontext("[1, 2, 3, 4, 5, 6]"),
            ),
            (
                (DoublyLinkedList([1, 2, 3]), DoublyLinkedList([1, 2, 3, 5])),
                nullcontext("[1, 2, 3, 1, 2, 3, 5]"),
            ),
            ((DoublyLinkedList([1, 2, 3]), 1), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), "123"), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), True), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), False), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), {1, 2, 3}), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), (1, 2, 3)), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), {"a": 1}), pytest.raises(TypeError)),
        ],
    )
    def test__add__(self, input, expectation):
        with expectation as string:
            (instance, addon) = input
            new_instance = instance + addon

            assert new_instance is not instance
            assert isinstance(new_instance, DoublyLinkedList)
            assert len(new_instance) == len(instance) + len(addon)
            assert str(new_instance) == string

            for index in range(len(instance)):
                assert instance[index] == new_instance[index]

            for index in range(-1, -len(addon) - 1, -1):
                assert addon[index] == new_instance[index]

    @pytest.mark.parametrize(
        "input, expectation",
        [
            ((DoublyLinkedList(), 0), nullcontext(("[]", 0))),
            ((DoublyLinkedList(), 2), nullcontext(("[]", 0))),
            ((DoublyLinkedList([1, 2, 3]), 0), nullcontext(("[]", 0))),
            ((DoublyLinkedList([1, 2, 3]), -1), nullcontext(("[]", 0))),
            ((DoublyLinkedList([1, 2, 3]), False), nullcontext(("[]", 0))),
            ((DoublyLinkedList([1, 2, 3]), 1), nullcontext(("[1, 2, 3]", 3))),
            ((DoublyLinkedList([1, 2, 3]), True), nullcontext(("[1, 2, 3]", 3))),
            ((DoublyLinkedList([1, 2, 3]), 2), nullcontext(("[1, 2, 3, 1, 2, 3]", 6))),
            ((DoublyLinkedList([1, 1]), 3), nullcontext(("[1, 1, 1, 1, 1, 1]", 6))),
            ((DoublyLinkedList([1]), 6), nullcontext(("[1, 1, 1, 1, 1, 1]", 6))),
            ((DoublyLinkedList([1]), "6"), pytest.raises(TypeError)),
            ((DoublyLinkedList([1]), (1,)), pytest.raises(TypeError)),
            ((DoublyLinkedList([1]), [1]), pytest.raises(TypeError)),
            ((DoublyLinkedList([1]), {}), pytest.raises(TypeError)),
            ((DoublyLinkedList([1]), set()), pytest.raises(TypeError)),
        ],
    )
    def test__mul__(self, input, expectation):
        with expectation as e:
            (instance, multiplier) = input
            new_instance = instance * multiplier

            assert new_instance is not instance
            assert isinstance(new_instance, DoublyLinkedList)

            (string, length) = e
            assert str(new_instance) == string
            assert len(new_instance) == length

            for index in range(len(new_instance)):
                assert new_instance[index] == instance[index % len(instance)]

    def test__repr__(self):
        assert repr(self.list) == "<DoublyLinkedList values: [1, 2, 3]>"

    def test__str__(self):
        assert str(self.list) == "[1, 2, 3]"

    @pytest.mark.parametrize(
        "input, expectation",
        [
            ((DoublyLinkedList(), 0), nullcontext(("[0]", 1, 0, 0))),
            ((DoublyLinkedList([1]), 2), nullcontext(("[1, 2]", 2, 1, 2))),
        ],
    )
    def test_append(self, input, expectation):
        with expectation as e:
            (instance, extension) = input
            instance.append(extension)

            (string, length, head, tail) = e
            assert str(instance) == string
            assert len(instance) == length
            assert instance.head.value == head
            assert instance.tail.value == tail

    @pytest.mark.parametrize(
        "input, expectation",
        [
            ((DoublyLinkedList([1]), None), nullcontext(("[]", 0, None, 1))),
            ((DoublyLinkedList([1, 2]), None), nullcontext(("[1]", 1, 1, 2))),
            ((DoublyLinkedList(), None), pytest.raises(AssertionError)),
            ((DoublyLinkedList([]), None), pytest.raises(AssertionError)),
            ((DoublyLinkedList([1]), 0), nullcontext(("[]", 0, None, 1))),
            ((DoublyLinkedList([1, 2]), 1), nullcontext(("[1]", 1, 1, 2))),
            ((DoublyLinkedList([1, 2]), 0), nullcontext(("[2]", 1, 2, 1))),
            ((DoublyLinkedList([1, 2, 3]), 1), nullcontext(("[1, 3]", 2, 3, 2))),
            ((DoublyLinkedList(), 0), pytest.raises(IndexError)),
            ((DoublyLinkedList(), 1), pytest.raises(IndexError)),
        ],
    )
    def test_pop(self, input, expectation):
        with expectation as e:
            (instance, index) = input
            res = instance.pop(index)

            (string, length, tail, result) = e
            assert str(instance) == string
            assert len(instance) == length
            assert res == result
            if instance.tail is not None:
                assert instance.tail.value == tail
            else:
                assert instance.tail == tail

    @pytest.mark.parametrize(
        "input, expectation",
        [
            ((DoublyLinkedList([]), 0, 1), nullcontext(("[1]", 1))),
            ((DoublyLinkedList([1]), 1, 2), nullcontext(("[1, 2]", 2))),
            ((DoublyLinkedList([1]), 0, 2), nullcontext(("[2, 1]", 2))),
            ((DoublyLinkedList([1]), -1, 2), nullcontext(("[2, 1]", 2))),
            ((DoublyLinkedList([1, 2, 3]), -1, 4), nullcontext(("[1, 2, 4, 3]", 4))),
            ((DoublyLinkedList([1, 2, 3]), -2, 4), nullcontext(("[1, 4, 2, 3]", 4))),
            ((DoublyLinkedList([1, 2, 3]), -3, 4), nullcontext(("[4, 1, 2, 3]", 4))),
            ((DoublyLinkedList(), None, 1), pytest.raises(TypeError)),
            ((DoublyLinkedList(), True, 1), pytest.raises(TypeError)),
            ((DoublyLinkedList(), False, 1), pytest.raises(TypeError)),
            ((DoublyLinkedList(), [1], 1), pytest.raises(TypeError)),
            ((DoublyLinkedList(), "1", 1), pytest.raises(TypeError)),
            ((DoublyLinkedList([]), 1, 1), pytest.raises(IndexError)),
            ((DoublyLinkedList([1]), 2, 2), pytest.raises(IndexError)),
            ((DoublyLinkedList([1, 2, 3]), -4, 4), pytest.raises(IndexError)),
        ],
    )
    def test_insert(self, input, expectation):
        with expectation as e:
            (instance, index, value) = input
            instance.insert(index, value)

            (string, length) = e
            assert str(instance) == string
            assert len(instance) == length

    @pytest.mark.parametrize(
        "input, expectation",
        [
            ((DoublyLinkedList([1]), 1), nullcontext(("[]", 0))),
            ((DoublyLinkedList(["1"]), "1"), nullcontext(("[]", 0))),
            ((DoublyLinkedList([True]), True), nullcontext(("[]", 0))),
            ((DoublyLinkedList([False]), False), nullcontext(("[]", 0))),
            ((DoublyLinkedList([None]), None), nullcontext(("[]", 0))),
            ((DoublyLinkedList([1, 1]), 1), nullcontext(("[1]", 1))),
            ((DoublyLinkedList([1, 2]), 2), nullcontext(("[1]", 1))),
            ((DoublyLinkedList([1, 2, 3]), 2), nullcontext(("[1, 3]", 2))),
            ((DoublyLinkedList([1, 2, 3, 2]), 2), nullcontext(("[1, 3, 2]", 3))),
            ((DoublyLinkedList([]), 1), pytest.raises(ValueError)),
            ((DoublyLinkedList([1]), 2), pytest.raises(ValueError)),
            ((DoublyLinkedList([1]), "1"), pytest.raises(ValueError)),
            ((DoublyLinkedList(["1"]), 1), pytest.raises(ValueError)),
        ],
    )
    def test_remove(self, input, expectation):
        with expectation as e:
            (instance, value) = input
            instance.remove(value)

            (string, length) = e
            assert str(instance) == string
            assert len(instance) == length

    @pytest.mark.parametrize(
        "input, expectation",
        [
            ((DoublyLinkedList([]), []), nullcontext("[]")),
            ((DoublyLinkedList([]), DoublyLinkedList([])), nullcontext("[]")),
            ((DoublyLinkedList([1, 2, 3]), []), nullcontext("[1, 2, 3]")),
            (
                (DoublyLinkedList([1, 2, 3]), DoublyLinkedList([])),
                nullcontext("[1, 2, 3]"),
            ),
            (
                (DoublyLinkedList([1, 2, 3]), [4, 5, 6]),
                nullcontext("[1, 2, 3, 4, 5, 6]"),
            ),
            (
                (DoublyLinkedList([1, 2, 3]), DoublyLinkedList([1, 2, 3, 5])),
                nullcontext("[1, 2, 3, 1, 2, 3, 5]"),
            ),
            ((DoublyLinkedList([1, 2, 3]), 1), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), "123"), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), True), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), False), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), {1, 2, 3}), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), (1, 2, 3)), pytest.raises(TypeError)),
            ((DoublyLinkedList([1, 2, 3]), {"a": 1}), pytest.raises(TypeError)),
        ],
    )
    def test_extend(self, input, expectation):
        with expectation as string:
            (instance, extension) = input
            original_copy = instance.copy()
            result = instance.extend(extension)

            assert result is instance
            assert len(result) == len(original_copy) + len(extension)
            assert str(result) == string

            for index in range(len(original_copy)):
                assert original_copy[index] == instance[index]

            for index in range(-1, -len(extension) - 1, -1):
                assert extension[index] == result[index]

    def test_copy(self):
        copy = self.list.copy()
        assert isinstance(copy, DoublyLinkedList)
        assert copy is not self.list
        assert len(copy) == len(self.list)
        for i in range(len(self.list)):
            assert copy[i] == self.list[i]

    def test_clear(self):
        instance = self.list.clear()
        assert isinstance(instance, DoublyLinkedList)
        assert instance is self.list
        assert len(self.list) == 0
        assert self.list.head is None
        assert self.list.tail is None

    @pytest.mark.parametrize(
        "index, expectation",
        [
            (0, nullcontext(True)),
            (1, nullcontext(True)),
            (2, nullcontext(True)),
            (-1, nullcontext(True)),
            (-2, nullcontext(True)),
            (-3, nullcontext(True)),
            ("0", pytest.raises(TypeError)),
            (True, pytest.raises(TypeError)),
            (False, pytest.raises(TypeError)),
            ([1], pytest.raises(TypeError)),
            (None, pytest.raises(TypeError)),
            (3, pytest.raises(IndexError)),
            (4, pytest.raises(IndexError)),
            (-4, pytest.raises(IndexError)),
        ],
    )
    def test__validate_index(self, index, expectation):
        with expectation as e:
            is_valid = self.list._validate_index(index)
            assert is_valid == e

    def test__get_node_at(self):
        for i in range(len(self.list)):
            node = self.list._get_node_at(i)
            assert node.value == i + 1

        self.list._tail = None
        self.list._head = None
        with pytest.raises(AssertionError):
            node = self.list._get_node_at(0)
            node = self.list._get_node_at(1)
            node = self.list._get_node_at(2)
