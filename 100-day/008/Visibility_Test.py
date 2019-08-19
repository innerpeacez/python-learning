class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar() # 强行访问私有变量
    print(test._Test__foo)
    # test.__bar()
    # print(test.__foo)
    pass


if __name__ == '__main__':
    main()
