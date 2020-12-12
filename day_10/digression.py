import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from timeit import default_timer as timer
from functools import lru_cache
from typing import NamedTuple

matplotlib.use('tkagg')


def fib_recursive(n: int) -> int:
    if n in (1, 2):
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


@lru_cache(maxsize=None)
def fib_recursive_with_memoization(n: int) -> int:
    if n in (1, 2):
        return 1
    else:
        return fib_recursive_with_memoization(n-1) + fib_recursive_with_memoization(n-2)


def fib_dynamic_programming(n: int) -> int:
    if n in (1, 2):
        return 1

    last, current = 1, 1

    for _ in range(2, n):
        last, current = current, current + last

    return current


class TimeSpent(NamedTuple):
    n: int
    time: float
    algorithm: str


if __name__ == '__main__':
    time_elapsed = []
    for i in range(1, 20):
        for _ in range(10):
            start = timer()
            result = fib_recursive(i)
            end = timer()
            time_elapsed.append(TimeSpent(n=i, time=1E3*(end - start), algorithm='recursive'))

            start = timer()
            result = fib_recursive_with_memoization(i)
            end = timer()
            time_elapsed.append(TimeSpent(n=i, time=1E3 * (end - start), algorithm='recursive (with cache)'))

            start = timer()
            result = fib_dynamic_programming(i)
            end = timer()
            time_elapsed.append(TimeSpent(n=i, time=1E3 * (end - start), algorithm='dynamic programming'))

    df = pd.DataFrame(data=time_elapsed,)
    ax = sns.lineplot(data=df, x='n', y='time', hue='algorithm')
    ax.set(xlabel='Number', ylabel='Time (ms)')
    plt.show()
