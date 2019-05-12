import search

def _test_search_algorithm(algorithm, preprocessor = lambda x: x):
    data = [4, 5, 3, 2, 1, 6]
    data = preprocessor(data)
    assert algorithm(data, 3)
    assert not algorithm(data, 7)


def test_linear_search():
    _test_search_algorithm(search.linear_search)


def test_binary_search():
    _test_search_algorithm(search.binary_search, sorted)