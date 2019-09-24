import bs4
import requests
from bs4 import BeautifulSoup as bs


def write_file():
    return open('the_best_university.txt', 'wd')


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(u_list, html):
    soup = bs(html, 'html.parser')
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            u_list.append([tds[0].string, tds[1].string, tds[2].string])


def printUnivList(u_list, num):
    tplt = "{0:^10}{1:{3}^10}{2:^10}"
    print(tplt.format("排名", "学校名称", "分数", chr(12288)))
    for i in range(num):
        u = u_list[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    html = getHtmlText(url)
    fillUnivList(u_info, html)
    printUnivList(u_info, 20)
    pass


if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    u_info = []

    main()
