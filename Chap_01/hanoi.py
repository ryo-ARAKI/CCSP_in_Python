from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_disks: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_disks + 1):  # Put disks on tower_a
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)  # Move upper n-1 disks from tower A to B using C as temporal
        hanoi(begin, end, temp, 1)  # Move bottom 1 disk from tower A to C
        hanoi(temp, end, begin, n - 1)  # Move n-1 disks from tower B to C by using A as temporal


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_disks)
    print(tower_a)
    print(tower_b)
    print(tower_c)
