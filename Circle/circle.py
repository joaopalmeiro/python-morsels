from math import pi


class Circle:
    def __init__(self, radius=1):
        # Code style: https://docs.python.org/3/library/functions.html#property
        self._radius = radius

    def __repr__(self):
        return f"Circle({self._radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = new_radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, new_diameter):
        # Here it is relevant to use `self.radius` instead of `self._radius`
        # in order to validate whether the new radius value, based on the
        # new diameter value, is positive.
        self.radius = new_diameter / 2

    @property
    def area(self):
        return pi * (self._radius ** 2)
