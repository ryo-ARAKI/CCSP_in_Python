def fib2(n: int) -> int:
    if n < 2:  # At basement
        return n
    return fib2(n - 1) + fib2(n - 2)


if __name__ == "__main__":
    print(fib2(5))
