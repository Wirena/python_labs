def func(seq):
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


def main():
    print(func([1989, 'dylan', 'jflex', 1968, 'sas']))


if __name__ == "__main__":
    main()
