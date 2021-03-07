"""Tests the Binary Search algorithm implementation."""

from src.search.binary import search
from test.util import create_test_runner

cases = [
  (([0,1,2,3,4,5,6,7,8,9], 8), 8),
  (([0,1,2,3,4,5,6,7,8,9], 9), 9),
  (([0,1,2,3,4,5,6,7,8,9], 10), -1),
  (([], 42), -1),
  (([0], 0), 0),
  (([0], 1), -1),
  (([0,1], 0), 0),
  (([0,1], 1), 1),
  (([0,1], 42), -1),
  (([0,1], 42), -1),
  (([0,1,2], 0), 0),
  (([0,1,2], 1), 1),
  (([0,1,2], 2), 2),
  (([0,1,2], 42), -1)
]

test = create_test_runner(search)
test(cases)