import requests
from bs4 import BeautifulSoup
import time


def getlist(list_url):
    time.sleep(2)
    res = requests.get(list_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    movie_list = soup.select('.grid_view li')
    for m in movie_list:
        rank = m.select('em')[0].text
        score = m.select('.rating_num')[0].text
        title = m.select('.title')[0].text
        direct = m.select('.info .bd p')[0].text.strip()
        actor = '\n主演:'.join(direct.split('   主演:'))
        director = '年代:'.join(actor.split('                           '))
        if m.select('.inq'):
            comments = m.select('.inq')[0].text.strip()
        else:
            comments = 'None'
        movie.append(
            '排名: ' + rank + '\n'
            + '评分: ' + score + '\n'
            + '片名: ' + title + '\n'
            + director + '\n'
            + '评论: ' + comments + '\n'
            + '\n')
    if soup.select('.next a'):
        asoup = soup.select('.next a')[0]['href']
        next_page = seed_url + asoup
        getlist(next_page)
    else:
        print('结束')
    return movie


def write(movies):
    with open('movie.txt', 'w', encoding='utf8') as m:
        for a in movies:
            m.write(a)


def main():
    write(getlist(seed_url))
    pass


if __name__ == '__main__':
    seed_url = 'https://movie.douban.com/top250'
    movie = []
    main()
