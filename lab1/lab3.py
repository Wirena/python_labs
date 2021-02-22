from math import *


def a(m: int, i: int) -> float:
    res = 0
    for j in range(1, m):
        res += sin(i) + pow(j, 5)
    return res


def b(n: int) -> float:
    res = 0
    for i in range(1, n):
        res += a(n)
    return res


def c(n: int) -> float:
    res = 0
    for i in range(1, n):
        res += pow(i, 8) / 26 + pow(3, i)
    return res


def func(n:int, m:int) -> float:
    return b(n)+c(n)


def main():
    print("{:.2e}".format(func(float(input()))))


if __name__ == "__main__":
    main()
