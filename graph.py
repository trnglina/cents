from sys import argv
from cents import calc
import matplotlib.pyplot as plt

if __name__ == "__main__":
    cents_str = " ".join(argv[3:])
    assert(cents_str[0] == "[")
    assert(cents_str[-1] == "]")

    frm = int(argv[1])
    until = int(argv[2]) + 1
    assert(until > frm)
    assert(frm > 0)

    fig = plt.figure()
    ax = fig.add_subplot()

    x = range(frm, until)
    y = [calc(i, [float(el.strip())
                  for el in cents_str[1:-1].split(",")]) for i in x]

    plt.plot(x, y, marker='o')

    for xy in zip(x, y):
        ax.annotate('%s' % xy[0], xy=xy, textcoords='data')

    plt.grid()
    plt.show()
