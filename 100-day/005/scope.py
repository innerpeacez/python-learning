def foo():
    b = 'hello'
    test()
    global a
    a = 200

    def bar():
        nonlocal b
        c = True
        print(a)
        print(b)
        print(c)
        b = 'world'

    print('b 的长度', len(b))
    bar()
    print(b)


def main():
    foo()
    print(a)
    pass


if __name__ == '__main__':
    a = 100


    def test():
        print("test")


    main()
