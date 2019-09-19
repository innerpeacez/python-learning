import requests


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'exception'


def main():
    print(get_html_text(url))
    pass


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    main()
