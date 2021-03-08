from math import *


def f(n: float) -> float:
    if n == 0:
        return 8
    elif n == 1:
        return 2
    return 1 / 13.0 * pow(f(n - 2), 2.0) + cos(f(n - 2))


def main():
    print("{:.2e}".format(f(float(input()))))


if __name__ == "__main__":
    main()
