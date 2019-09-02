from random import randint
from threading import Thread
from time import sleep, time


def download(filename):
    print('开始下载 %s ...' % filename)
    download_time = randint(5, 10)
    sleep(download_time)
    print('%s 下载完成! 耗时%d 秒' % (filename, download_time))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python thread multi.jpg',))
    t2 = Thread(target=download, args=('Hello Python.jpg',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总耗时:%.3f秒' % (end - start))

    pass


if __name__ == '__main__':
    main()
