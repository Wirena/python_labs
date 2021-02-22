from math import *


def func(x: float, y: float) -> float:
    res = (77 * pow(y, 5) - 92 * pow(y, 4)) / (pow(y, 4) + pow(y, 6))
    res -= log(70 * pow(x, 5)) - pow(y, 6) / 38
    res -= cos(log(x) - abs(y) + 87) + 33 * y
    return res


def main():
    print("{:.2e}".format(func(float(input()), float(input()))))


if __name__ == "__main__":
    main()
