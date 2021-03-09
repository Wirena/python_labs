def code(n: int) -> int:
    g = (n & 0x80000000) >> 31
    f = (n & 0x40000000) >> 29
    e = (n & 0x30000000) >> 26
    d = (n & 0xFF00000) >> 16
    c = (n & 0xF8000) >> 3
    b = (n & 0x7FFC) << 17
    a = (n & 0x3) << 17
    return a + b + c + d + e + f + g


def main():
    print(hex(code(0xa0fce2b0)))


if __name__ == "__main__":
    main()
