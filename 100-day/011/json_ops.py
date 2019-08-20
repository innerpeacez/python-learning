import json


def main():
    mydict = {
        'name': 'innerpeacez',
        'age': 18,
        'qq': 10146749,
        'friends': ['王大锤', '李元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as ex:
        print(ex)

    print('保存数据完成')
    pass


if __name__ == '__main__':
    main()
