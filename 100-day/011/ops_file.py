def main():
    file = None
    try:
        with open('hello_open.txt', 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('文件不存在')
    except LookupError:
        print('未知编码错误')
    except UnicodeDecodeError:
        print('文件解码错误')


if __name__ == '__main__':
    main()
