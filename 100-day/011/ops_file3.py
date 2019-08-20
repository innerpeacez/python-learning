from math import sqrt


def is_prime(number):
    """
    判断是否为素数
    :param number:
    :return:
    """

    assert number > 0
    for factor in range(2, int(sqrt(number)) + 1):
        if number % factor == 0:
            return False
    return True if number != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))

        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件发生错误')

    print('操作完成')


if __name__ == '__main__':
    main()
