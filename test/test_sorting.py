import random

from sorting import selection_sort, insertion_sort, bubble_sort


def _test_sort_algorithm(algorithm):
    input_array = [random.random() * 10000000 for _ in range(1000)]
    expected_result = sorted(input_array)
    assert algorithm(input_array) == expected_result


def test_selection_sort():
    _test_sort_algorithm(selection_sort)


def test_insertion_sort():
    _test_sort_algorithm(insertion_sort)


def test_bubble_sort():
    _test_sort_algorithm(bubble_sort)
