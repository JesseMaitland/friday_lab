from pathlib import Path
from typing import Callable
from argparse import Namespace
from spam.src import FileManager



# def init_redscope_env(provide_config: bool = False):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             load_redscope_env()
#             if provide_config:
#                 return func(config=get_redscope_config(), *args, **kwargs)
#             else:
#                 return func(*args, **kwargs)
#         return wrapper
#     return


def my_decorator_with_args(arg1: bool = False):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            print(arg1)
            print("wooo hoooo!!!!")
            return func(*args, **kwargs)
        return wrapper
    return decorator



@my_decorator_with_args(arg1=True)
def beans(cmd: Namespace) -> None:
    print("blah!")

