import sys


def main():
    # 定义元组
    t = ('innerpeacez', '18', 1, '杭州')
    print(t)
    for info in t:
        print(info)

    # 尝试给元组赋值
    # t[0] = 'xx'
    # t = ('王大锤', 20, True, '云南昆明')  # 原来的元组将被垃圾回收
    # print(t)

    # 元组与列表的相互转换
    person = list(t)

    print(person)
    person[0] = 'zhw'
    print(person)
    t2 = tuple(person)

    print(t2)

    _list = ['innerpeacez', '18', 1, '杭州']
    _tuple = ('innerpeacez', '18', 1, '杭州')

    # tuple 的创建时间和占用空间优于列表
    print(sys.getsizeof(_list))
    print(sys.getsizeof(_tuple))
    pass


if __name__ == '__main__':
    main()
