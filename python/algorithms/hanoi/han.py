__author__ = 'igomez'


def hanoi(source, auxiliar, to, h=8):
    if h >= 1:
        hanoi(source, to, auxiliar, h - 1)
        to.append(source.pop())
        hanoi(auxiliar, source, to, h - 1)


def main():
    source = [8, 7, 6, 5, 4, 3, 2, 1]
    auxiliar = []
    to = []

    hanoi(source, auxiliar, to)

    print to


if __name__ == '__main__':
    main()
