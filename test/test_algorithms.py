import random

from inversions import brute_force_inversion_counter, inversions_counter


def test_inversion_counter():
    test_array = [1, 3, 5, 2, 4, 6]
    assert inversions_counter(test_array) == 3


def test_inversion_using_brute_force():
    test_array = [1, 3, 5, 2, 4, 6]
    assert brute_force_inversion_counter(test_array) == 3


def test_inversion_counter_on_random_array():
    input_array = [random.random() * 10000000 for _ in range(1000)]
    assert brute_force_inversion_counter(input_array) == inversions_counter(input_array)
