from math import *


def a(m: int, i: int) -> float:
    res = 0
    for j in range(1, m+1):
        res += sin(i) + pow(j, 5)
    return res


def b(n: int, m: int) -> float:
    res = 0
    for i in range(1, n+1):
        res += a(m, i)
    return res


def c(n: int) -> float:
    res = 0
    for i in range(1, n+1):
        res += pow(i, 8) / 26.0 + pow(i, 3)
    return res


def func(n: int, m: int) -> float:
    return b(n, m) + c(n)


def main():
    print("{:.2e}".format(func(int(input()), int(input()))))


if __name__ == "__main__":
    main()
