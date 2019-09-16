from redis.sentinel import Sentinel


def conn():
    sentinel = Sentinel([('192.168.10.196', 30671), ('192.168.10.196', 30459), ('192.168.10.196', 30396)],
                        socket_timeout=0.5)
    return sentinel


def main():
    sentinel = conn()
    master = sentinel.discover_master('mymaster')
    slaves = sentinel.discover_slaves('mymaster')

    print(f'master:{master}')
    print(f'slaves:{slaves}')
    pass


if __name__ == '__main__':
    main()
