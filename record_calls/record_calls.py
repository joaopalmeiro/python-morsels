from dataclasses import dataclass
from functools import partial, wraps
from typing import Any, Dict, List

NO_RETURN = object()

println = partial(print, end="\n" * 2)


@dataclass(frozen=True)  # Immutable
class Call:
    args: List
    kwargs: Dict
    return_value: Any
    exception: Any


def record_calls(func):
    @wraps(func)
    def wrapper_record_calls(*args, **kwargs):
        wrapper_record_calls.call_count += 1

        try:
            value = func(*args, **kwargs)
            wrapper_record_calls.calls.append(Call(args, kwargs, value, None))
            return value
        except Exception as e:
            wrapper_record_calls.calls.append(Call(args, kwargs, NO_RETURN, e))
            raise e

    # More info: https://www.youtube.com/watch?v=9oyr0mocZTg
    wrapper_record_calls.call_count = 0
    wrapper_record_calls.calls = []

    return wrapper_record_calls


# @record_calls
# def greet(name="World"):
#     println(f"Hello, {name}!")


# @record_calls
# def cube(n):
#     return n ** 3


# help(greet)
# greet()
# println(greet.call_count)
# greet()
# println(greet.call_count)
# greet()
# println(greet.call_count)

# println(greet.calls[0].args)
# println(greet.calls[0].kwargs)

# cube(3)
# println(cube.calls)
# cube(None)
# println(cube.calls[-1].exception)
# println(cube.calls[-1].return_value == NO_RETURN)
