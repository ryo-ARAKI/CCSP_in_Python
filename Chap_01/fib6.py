from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # At basement
    if n > 0: yield 1  # At basement
    lastval: int = 0  # Initial value: fib(0)
    nextval: int = 1  # Initial value: fib(1)
    for _ in range(1, n):
        lastval, nextval = nextval, lastval + nextval  # Using tuple unpack
        yield nextval  # Main generator step


if __name__ == "__main__":
    for i in fib6(50):
        print(i)
