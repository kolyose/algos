"""Tests the Binary Search algorithm implementation."""

import pytest

from src.search.binary import search

cases = [
    (([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 8),
    (([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9),
    (([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), -1),
    (([], 42), -1),
    (([0], 0), 0),
    (([0], 1), -1),
    (([0, 1], 0), 0),
    (([0, 1], 1), 1),
    (([0, 1], 42), -1),
    (([0, 1], 42), -1),
    (([0, 1, 2], 0), 0),
    (([0, 1, 2], 1), 1),
    (([0, 1, 2], 2), 2),
    (([0, 1, 2], 42), -1),
]


@pytest.mark.parametrize("input,expected", cases)
def test_search(input, expected):
    assert search(*input) == expected
