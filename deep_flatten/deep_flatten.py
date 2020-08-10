from collections.abc import Iterable
from typing import Iterator


def deep_flatten(lst: Iterable) -> Iterator[Iterable]:
    for el in lst:
        if isinstance(el, Iterable) and not isinstance(el, str):
            yield from deep_flatten(el)
        else:
            yield el
