def main():
    file = None
    try:
        # 一次性读取整个文件内容
        with open('hello_open.txt', 'r', encoding='utf-8') as file:
            print(file.read())
        print('______________________________________')
        with open('hello_open.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line)
        print('______________________________________')
        with open('hello_open.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(lines)
    except FileNotFoundError:
        print('文件不存在')
    except LookupError:
        print('未知编码错误')
    except UnicodeDecodeError:
        print('文件解码错误')


if __name__ == '__main__':
    main()
