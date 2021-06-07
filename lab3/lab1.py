import struct

size_a = 2 + 4 + 4 + 4 + 4 + 2 + 2

size_b = 4 + 2 + 2
size_c = 5 + 2
size_d = 4 + 1 + 1 + 2 + 2 + 32

offset_b: int
offset_c: int
number_c: int
offset_d: int


def parse_b(bytes, offset):
    bytes_b = bytes[offset:offset + size_b]
    parsed = struct.unpack("=fhH", bytes_b)
    return {"B1": parsed[0], "B2": parsed[1], "B3": parsed[2]}


def parse_c(bytes, offset):
    bytes_c = bytes[offset:offset + size_c]
    parsed = struct.unpack("=cccccH", bytes_c)
    return {"C1": b''.join(parsed[0:5]).decode("utf-8"), "C2": parse_d(bytes, parsed[5])}


def parse_d(bytes, offset):
    bytes_d = bytes[offset:offset + size_d]
    parsed = struct.unpack("=iBBHHiiiiiiii", bytes_d)
    arr = list(struct.unpack("=" + "I" * parsed[3], bytes[parsed[4]:parsed[4] + 4 * parsed[3]]))
    return {"D1": parsed[0], "D2": parsed[1], "D3": parsed[2], "D4": arr, "D5": list(parsed[5:])}


def parse_a(bytes, offset):
    bytes_a = bytes[offset:offset + size_a]
    parsed = struct.unpack("=HiffIHH", bytes_a)
    offset_b = parsed[0];
    offset_c = parsed[6]
    number_c = parsed[5]
    arr = struct.unpack("I" * parsed[4], bytes[parsed[5]:parsed[5] + parsed[4]*4])
    return {"A1": parse_b(bytes, parsed[0]), "A2": parsed[1], "A3": parsed[2], "A4": parsed[3],
            "A5": [parse_c(bytes, addr) for addr in arr], "A6": parsed[6]}


def f31(bytes: bytes):
    return parse_a(bytes, 5)



