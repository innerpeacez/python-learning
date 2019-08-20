import re


def main():
    phone_number_pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    content = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。'''
    phone_numbers = re.findall(phone_number_pattern, content)
    print(phone_numbers)

    print('--------------------------------')
    for number in phone_number_pattern.finditer(content):
        print(number.group())
    print('--------------------------------')

    m = phone_number_pattern.search(content)
    while m:
        print(m.group())
        m = phone_number_pattern.search(content, m.end())

    pass


if __name__ == '__main__':
    main()
