from collections.abc import Iterable
from typing import Iterator


def deep_flatten(lst: Iterable) -> Iterator[Iterable]:
    for el in lst:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from deep_flatten(el)
        else:
            yield el


# print(list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])))
# print(list(deep_flatten([["apple", "pickle"], ["pear", "avocado"]])))

# numbers_and_words = enumerate([99, 98, 97])
# flattened = deep_flatten(numbers_and_words)
# print(next(numbers_and_words))
# print(next(flattened))
# print(next(flattened))
