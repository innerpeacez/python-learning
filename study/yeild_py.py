def foo():
    print("starting ...")
    while True:
        res = yield 4
        print("res:", res)


def main():
    # g = foo()
    # print(next(g))

    # print("*" * 20)
    # print(next(g))
    # print(next(g))
    # print(g.send(7))
    # iterator_yield_list()
    # g = yield_list(10)
    # print(next(g))
    range_yield_list()


def yield_list(n):
    print("yield starting...")
    while n > 0:
        yield n
        n -= 1


def iterator_yield_list():
    for n in yield_list(10):
        print(n)


def range_yield_list():
    g = yield_list(10)
    for n in range(next(g)):
        print(n)


if __name__ == '__main__':
    main()
