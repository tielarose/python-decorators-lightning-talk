import functools
from datetime import datetime, time


def only_on_a_certain_day(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if datetime.now().weekday() == 4:
            return func(*args, **kwargs)
    return wrapper


def time_my_func(func):
    @functools.wrap(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        the_func = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('Finished {func.__name__} in {run_time} seconds')
        return the_func
    return wrapper


def debug_this(func):
    @functools.wrap
    def wrapper(*args, **kwargs):
        print(f'debug_this: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'debug_this: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper
