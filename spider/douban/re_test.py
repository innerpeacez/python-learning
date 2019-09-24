import re


def main():
    text = '(\t        523543人评价 \t)'
    regex = re.compile(r'[\d]{1,10}')
    print(regex.findall(text))
    pass


if __name__ == '__main__':
    main()
