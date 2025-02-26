"""Tests the Merge Sort algorithm implementation."""

import pytest
from src.sort.radix import sort

cases = [
    (([],), []),
    (([1],), [1]),
    (([1, -1, 0],), [-1, 0, 1]),
    (([-1, -2],), [-2, -1]),
    (([1, 2, 1],), [1, 1, 2]),
    (([0, -5, 4, 9, 11, 0],), [-5, 0, 0, 4, 9, 11]),
    (
        ([0, -5, -5, 4, 9, 22, 123, -10, -68, -148, -4321, 666, 666, 1234, 10000, 0],),
        [-4321, -148, -68, -10, -5, -5, 0, 0, 4, 9, 22, 123, 666, 666, 1234, 10000],
    ),
]


@pytest.mark.parametrize("input,expected", cases)
def test_sort(input, expected):
    assert sort(*input) == expected
