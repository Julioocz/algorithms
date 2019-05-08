from decimal import *


def to_digits(number):
    if isinstance(number, list):
        return number

    return list(map(int, str(number)))


def pad_zero_left(digits, wanted_len):
    padding = wanted_len - len(digits)
    if padding <= 0:
        return digits

    return [0] * padding + digits


def exp(digits, n):
    return digits + [0] * n


def to_number(digits):
    return int("".join(map(str, digits)))


def to_same_len(x, y):
    max_len = max(len(x), len(y))
    return pad_zero_left(x, max_len), pad_zero_left(y, max_len)


def to_same_even_len(x, y):
    max_len = max(len(x), len(y))
    if max_len % 2 != 0:
        max_len += 1
    return pad_zero_left(x, max_len), pad_zero_left(y, max_len)


def sum_digits(x, y):
    return to_digits(to_number(x) + to_number(y))


def count_digits(number):
    return len(str(number))


def decompose_simple(number_array):
    if len(number_array) == 1:
        return number_array[0]

    if len(number_array) > 2:
        raise ValueError("Decompose simple should only be used with two digits")

    a, b = number_array
    return 10 * a + b


def karatsuba_multiplication(x, y):
    n = len(x)
    half_n = int(n / 2)
    a, b = x[:half_n], x[half_n:]
    c, d = y[:half_n], y[half_n:]
    first_term = mul(a, c)
    second_term = mul(b, d)
    third_term = mul(sum_digits(a, b), sum_digits(c, d)) - first_term - second_term
    return 10 ** n * first_term + 10 ** (n / 2) * third_term + second_term


def recursive_integer_multiplication(x, y):
    n = len(x)
    m = len(y)
    half_n = n // 2
    half_m = m // 2
    a, b = x[:half_n], x[half_n:]
    c, d = y[:half_m], y[half_m:]
    ac = mul(a, c)
    ad = mul(a, d)
    bc = mul(b, c)
    bd = mul(b, d)
    return 10 ** ((n + m) / 2) * ac + 10 ** (n / 2) * ad + 10 ** (m / 2) * bc + bd


def mul(x, y):
    if not isinstance(x, list) or not isinstance(y, list):
        return mul(to_digits(x), to_digits(y))

    if len(x) == 1 or len(y) == 1:
        return to_number(x) * to_number(y)

    if len(x) != len(y) or len(x) % 2 != 0 or len(y) % 2 != 0:
        x, y = to_same_even_len(x, y)

    return recursive_integer_multiplication(x, y)
