from itertools import zip_longest
from typing import List


# While the `zip` function stops at the shortest list,
# the `zip_longest` function stops at the longest one
# and uses a `fillvalue` for the missing items. Thus,
# when using the default `fillvalue` (`None`), an error
# (`TypeError`) will be thrown when `None` is added to
# a number or an attempt is made to loop over `None`.
def add(*matrices: List[List[int]]) -> List[List[int]]:
    try:
        return [
            [sum(elements) for elements in zip_longest(*rows, fillvalue=None)]
            for rows in zip_longest(*matrices, fillvalue=None)
        ]
    except TypeError as e:
        raise ValueError("Given matrices are not the same size.") from e


# matrix1 = [[1, 9], [7, 3]]
# matrix2 = [[5, -4], [3, 3]]
# matrix3 = [[2, 3], [-3, 1]]

# print(add(matrix1, matrix2, matrix3))  # [[8, 8], [7, 7]]
