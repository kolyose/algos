"""Tests the Bubble Sort algorithm implementation."""

import pytest

from src.sort.bubble import sort

cases = [
    (([],), []),
    (([1],), [1]),
    (([1, -1, 0],), [-1, 0, 1]),
    (([-1, -2],), [-2, -1]),
    (([1, 2, 1],), [1, 1, 2]),
    (([0, -5, 4, 9, 11, 0],), [-5, 0, 0, 4, 9, 11]),
]


@pytest.mark.parametrize("input,expected", cases)
def test_sort(input, expected):
    assert sort(*input) == expected
