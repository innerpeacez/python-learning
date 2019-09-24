import bs4
import requests
import re
from bs4 import BeautifulSoup
from operator import itemgetter


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parserText(text, book_list):
    soup = BeautifulSoup(text, 'html.parser')
    for table in soup('table', {'width': '100%'}):
        if isinstance(table, bs4.element.Tag):
            tds = table.find('tr')('td')
            divs = tds[1]('div')
            content = {}
            for div in divs:
                if isinstance(div, bs4.element.Tag):
                    if div.find('a'):
                        name = div.find('a').attrs['title']
                        content.update({"书名": name})
                    if div.select('.rating_nums'):
                        score = div.select('.rating_nums')[0].text
                        content.update({"评分": score})
                    if div.select('.pl'):
                        people_num = div.select('.pl')[0].text
                        regex = re.compile(r'[\d]{1,10}')
                        content.update({"评价人数": regex.findall(people_num)[0]})

            ps = tds[1]('p')
            for p in ps:
                if isinstance(p, bs4.element.Tag):
                    if p.attrs['class'][0] == 'quote':
                        description = p.find('span').string
                        content.update({"介绍": description})
                    if p.attrs['class'][0] == 'pl':
                        author = p.string
                        content.update({"作者信息": author})

            book_list.append(content)

    next_books = soup.find('span', {'class': 'next'})
    if next_books.find('a'):
        a = next_books.find('a').attrs['href']
        text = getHtmlText(a)
        parserText(text, books)

    return book_list


def sorted_boot_top250(book_list):
    tmp = sorted(book_list, key=itemgetter('评分'), reverse=True)
    for i in range(len(tmp)):
        tmp[i].update({"排名": i + 1})
    return tmp


def writeToFile(book_list):
    with open('good_books.txt', 'w', encoding='utf8') as book_file:
        for book in book_list:
            for key, value in book.items():
                book_file.write(f'{key}:{value}\n')
            book_file.write('\n')
    pass


def main():
    text = getHtmlText(seed_url)
    book_list = parserText(text, books)
    writeToFile(sorted_boot_top250(book_list))
    pass


if __name__ == '__main__':
    seed_url = "https://book.douban.com/top250"
    books = []
    main()
