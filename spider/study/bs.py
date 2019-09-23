import requests
from bs4 import BeautifulSoup


def main():
    r = requests.get('https://python123.io/ws/demo.html')
    print(r.text[-500:])

    demo = r.text

    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.prettify())
    print(soup.title)
    print(soup.a)
    tag = soup.a
    print(soup.a.parent)
    print(tag.attrs)

    print('------------------------------')
    print(soup.head)
    print(soup.head.contents)
    print('------------------------------')
    print(soup.body.contents)
    print(len(soup.body.contents))


if __name__ == '__main__':
    main()
