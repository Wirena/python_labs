from math import *


def f11(x: float, y: float) -> float:
    res = (77 * pow(y, 5) - 92 * pow(y, 4)) / (pow(y, 4) + pow(y, 6))
    res -= log(70 * pow(x, 5)) - pow(y, 6) / 38
    res -= cos(log(x) - abs(y) + 87) + 33 * y
    return res


def f12(x: float) -> float:
    def a(x: float) -> float:
        return 72 * pow(x, 4) + cos(x)

    def b(x: float) -> float:
        return tan(pow(x, 8) - pow(x, 6) + pow(x, 6))

    def c(x: float) -> float:
        return pow(x, 4) - pow(x, 2)

    if x < 95:
        return a(x)
    if 95 <= x < 122:
        return b(x)
    return c(x)


def f13(n: int, m: int) -> float:
    def a(m: int, i: int) -> float:
        res = 0
        for j in range(1, m + 1):
            res += sin(i) + pow(j, 5)
        return res

    def b(n: int, m: int) -> float:
        res = 0
        for i in range(1, n + 1):
            res += a(m, i)
        return res

    def c(n: int) -> float:
        res = 0
        for i in range(1, n + 1):
            res += pow(i, 8) / 26.0 + pow(i, 3)
        return res

    return b(n, m) + c(n)


def f14(n: float) -> float:
    if n == 0:
        return 8
    elif n == 1:
        return 2
    return 1 / 13.0 * pow(f14(n - 2), 2.0) + cos(f14(n - 2))


def f21(seq):
    if seq[4] == "rhtml":
        return 11
    elif seq[4] == "sas":
        if seq[2] == "jflex":
            return 4
        elif seq[2] == "d":
            if seq[1] == "dylan":
                return 3
            elif seq[1] == "numpy":
                return 2
            elif seq[1] == "cuda":
                if seq[0] == 1989:
                    return 0
                elif seq[0] == 1957:
                    return 1
        elif seq[2] == "minid":
            if seq[1] == "dylan":
                if seq[0] == 1989:
                    return 9
                elif seq[0] == 1957:
                    return 10
            elif seq[1] == "numpy":
                if seq[3] == 1989:
                    return 6
                elif seq[3] == 1968:
                    return 7
                elif seq[3] == 2002:
                    return 8
            elif seq[1] == "cuda":
                return 5
    return -1


def f22(n: int) -> int:
    g = (n & 0x80000000) >> 31
    f = (n & 0x40000000) >> 29
    e = (n & 0x30000000) >> 26
    d = (n & 0xFF00000) >> 16
    c = (n & 0xF8000) >> 3
    b = (n & 0x7FFC) << 17
    a = (n & 0x3) << 17
    return a + b + c + d + e + f + g


def f23(table: list) -> list:
    formatted_table: list = []
    for i in range(0, len(table)):
        for j in range(i + 1, len(table)):
            if table[i] is not None and table[j] is not None:
                if table[i][0] == table[j][0]:
                    table[j] = None
    for entity in table:
        if entity is None or entity[0] == "":
            continue
        else:
            mail = str(entity[0]).split("[")[0]
            phone = str(entity[0]).split(";")[1]
            phone = "(" + phone[2:5] + ") " + phone[6:9] + "-" + phone[9:14]
            date_to_format = str(entity[1]).split(".")
            date = date_to_format[2] + "/" + date_to_format[1] + "/" + date_to_format[0]
            formatted_table.append([mail, phone, date])
    return formatted_table
