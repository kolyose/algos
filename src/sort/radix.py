from math import floor, log10
from typing import List


def get_digit_at(num: int, index: int) -> int:
    return num // 10**index % 10


def get_word_size(num: int) -> int:
    if num == 0:
        return 1

    return floor(log10(abs(num))) + 1


def is_negative(num: int) -> bool:
    return bool(abs(num) - num)


def sort(array):
    """Implement Radix Sort algorithm.

    Complexity:
      Time: O(n * w) - where n is number of elements in the array, and w is the highest word size (the highest number of digits in a number)
      Space: O(n + w)

    Arguments:
      - array - a list of integers to sort

    Returns:
      The sorted list
    """
    iterations_count = 1
    for item in array:
        iterations_count = max(iterations_count, get_word_size(item))

    for i in range(0, iterations_count):
        positive_buckets: List[List[int]] = [[] for _ in range(10)]
        negative_buckets: List[List[int]] = [[] for _ in range(10)]

        for item in array:
            buckets = negative_buckets if is_negative(item) else positive_buckets
            digit = get_digit_at(item, i)
            buckets[digit].append(item)

        array = [
            item for bucket in (negative_buckets + positive_buckets) for item in bucket
        ]

    return array
