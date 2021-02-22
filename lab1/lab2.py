from math import *


def a(x: float) -> float:
    return 72 * pow(x, 4) + cos(x)


def b(x: float) -> float:
    return tan(pow(x, 8) - pow(x, 6) + pow(x, 6))


def c(x: float) -> float:
    return pow(x, 4) - pow(x, 2)


def func(x: float) -> float:
    if x < 95:
        return a(x)
    if 95 <= x < 122:
        return b(x)
    return c(x)


def main():
    print("{:.2e}".format(func(float(input()))))


if __name__ == "__main__":
    main()
