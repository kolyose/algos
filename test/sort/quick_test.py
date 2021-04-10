"""Tests the Quick Sort algorithm implementations."""

from src.sort import quick_lomuto
from test.util import create_test_runner

cases = [
  (([],), []),
  (([1],), [1]),
  (([1, -1, 0],), [-1, 0, 1]),
  (([-1, -2],), [-2, -1]),
  (([1, 2, 1],), [1, 1, 2]),
  (([0, -5, 4, 9, 11, 0],), [-5, 0, 0, 4, 9, 11])
] 

test = create_test_runner(quick_lomuto.sort)
test(cases)