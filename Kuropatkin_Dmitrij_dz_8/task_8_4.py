from functools import wraps


def val_checker(l_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f'wrong value: {num}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(-5)
