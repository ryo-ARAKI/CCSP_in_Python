from functools import lru_cache  # Use cache to speed up


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:  # At basement
        return n
    return fib4(n - 1) + fib4(n - 2)


if __name__ == "__main__":
    print(fib4(50))
