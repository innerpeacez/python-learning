from multiprocessing import Process, Queue
from os import getpid
from time import sleep


def sub_task(string, q):
    print('启动下载进程，进程号[%d].' % getpid())
    count = q.get()
    while count < 10:
        print(string, end='', flush=True)
        count += 1
        q.put(count)
        count = q.get()
        print('q 中的count 值\n', count)
        sleep(0.01)


def main():
    count = 0
    q = Queue()
    q.put(count)
    p2 = Process(target=sub_task, args=('Pong', q))
    p1 = Process(target=sub_task, args=('Ping', q))
    p2.start()
    p1.start()
    p1.join()
    p2.join()
    pass


if __name__ == '__main__':
    main()
