from sys import argv


def nearest(n, collection):
    return min(collection, key=lambda x: abs(x - n))


def calc(divisions, cents):
    eqt = [n * (1200.0 / divisions) for n in range(1, divisions + 1)]
    return sum([abs(n - nearest(n, eqt)) for n in cents])


if __name__ == "__main__":
    cents_str = " ".join(argv[2:])
    assert(cents_str[0] == "[")
    assert(cents_str[-1] == "]")

    divisions = int(argv[1])
    assert(divisions > 0)

    cents = [float(el.strip()) for el in cents_str[1:-1].split(",")]
    print(calc(divisions, cents))
