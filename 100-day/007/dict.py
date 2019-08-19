def main():
    # 创建字典
    m = {"name": "innerpeacez", "age": 18, "sex": "male", "address": "hangzhou"}
    print(m)

    for key in m:
        print(f'key:{key},value:{m[key]}')

    # 更新
    m['address'] = 'China Hangzhou'

    print(m)

    m.update(address='Zhejiang Hangzhou China')
    m.update(addres='Zhejiang Hangzhou China')  # 如果key 不存在会添加新key
    print(m)

    # 删除元素
    print("删除元素》》》》》》》》》》》》》》》》》》》")
    m.popitem()
    m.pop('address')
    print(m)

    pass


if __name__ == '__main__':
    main()
