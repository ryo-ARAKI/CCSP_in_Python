def fib5(n: int) -> int:
    if n == 0: return n  # At basement
    lastval: int = 0  # Initial value: fib(0)
    nextval: int = 1  # Initial value: fib(1)
    for _ in range(1, n):
        lastval, nextval = nextval, lastval + nextval  # Using tuple unpack
    return nextval


if __name__ == "__main__":
    print(fib5(50))
