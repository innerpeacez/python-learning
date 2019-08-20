import re


def main():
    username = input('请输入用户名：')
    qq = input('请输入QQ号码：')
    regex1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not regex1:
        print('请输入有效的用户名')
    regex2 = re.match(r'^[1-9]\d{4,10}$', qq)
    if not regex2:
        print('请输入有效的QQ号')
    if regex1 and regex2:
        print('你的输入是有效的')

    pass


if __name__ == '__main__':
    main()
