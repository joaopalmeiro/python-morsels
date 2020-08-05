from dataclasses import dataclass
from functools import partial, wraps
from typing import Any, Optional

NO_RETURN = object()  # Sentinel object

println = partial(print, end="\n" * 2)


# `BaseException`: The base class for all Python built-in exceptions.
@dataclass(frozen=True)  # Immutable
class Call:
    args: tuple
    kwargs: dict
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None  # or `Any`


# Decorator: A callable that accepts a callable and returns a callable.
# Decorators can also be implemented as classes.
def record_calls(func):
    @wraps(func)
    def wrapper_record_calls(*args, **kwargs):
        wrapper_record_calls.call_count += 1

        try:
            value = func(*args, **kwargs)
            wrapper_record_calls.calls.append(Call(args, kwargs, return_value=value))
        except BaseException as e:
            wrapper_record_calls.calls.append(Call(args, kwargs, exception=e))
            raise  # No need to use `raise e`
        return value

    # More info: https://www.youtube.com/watch?v=9oyr0mocZTg.
    # Functions can have attributes.
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
