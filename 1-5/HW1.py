# DECORATORS

import time
import functools
import sys
from collections import OrderedDict


def profile(msg="Elapsed time for function"):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            start = time.time()
            deco._num_call += 1
            result = f(*args, **kwargs)
            deco._num_call -= 1

            if deco._num_call == 0:
                print(msg, f'{f.__name__}: {time.time() - start}s')
            return result

        deco._num_call = 0
        return deco

    return internal

# def cache(max_limit=64):
#     def internal(f):
#         @functools.wraps(f)
#         def deco(*args):
#             if args in deco._cache:
#                 deco._cache.move_to_end(args, last=True) # Перемещение только что использованного элемента в конец списка на удаление
#                 return deco._cache[args]
#             result = f(*args)
#             # Удаление из словаря значения, если в нем больше чем задано max_limit. Для Домашнего задания
#             if len(deco._cache) >= max_limit:
#                 deco._cache.popitem(last=False) # Использование collections.OrderedDict чуть укоротило код - все так же удаление первого элемента
#             deco._cache[args] = result
#             return result
#         deco._cache = OrderedDict()
#         return deco
#     return internal

def cache(max_size=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            if args in deco._cache:
                return deco._cache[args]
            if len(deco._cache) >= max_size:
                deco._cache.pop(next(iter(deco._cache)))
            result = f(*args)
            deco._cache[args] = result
            return result

        deco._cache = {}

        return deco

    return internal


@profile()
@cache(max_size=64)
# @cache
def fibo(n):
    """Super inefficient fibo function"""
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


for i in range(1000):
    print(i, '->', fibo(i))
# print(fibo(100))
print(fibo._cache)
print(len(fibo._cache))
