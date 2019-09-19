import requests


def main():
    r = requests.get('https://www.bilibili.com')
    print(r.status_code)
    print(r.encoding)
    print(r.apparent_encoding)
    r.encoding = r.apparent_encoding
    print(r.text)


if __name__ == '__main__':
    main()
