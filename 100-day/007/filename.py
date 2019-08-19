def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1  # python 中的三元表达式形式
        return filename[index:]
    else:
        return ''


def main():
    filename = get_suffix("text.txt", True)
    print(filename)
    pass


if __name__ == '__main__':
    main()
