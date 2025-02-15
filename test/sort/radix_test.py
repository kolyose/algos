"""Tests the Merge Sort algorithm implementation."""

from src.sort import radix
from test.util import create_test_runner

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

test = create_test_runner(radix.sort)
test(cases)
