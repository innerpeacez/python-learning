def main():
    list1 = [1, 2, 3, 4, 5, 6]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    # 计算列表长度(元素个数)
    print(len(list1))
    # 下标(索引)运算
    print(list1[0])
    print(list1[4])
    print(">>>>>>>>>>>>>>>")
    print(list1[-1])
    print(list1[-3])
    # print(list1[7])

    # 赋值运算
    list1[2] = 300
    print(list1)
    # 末尾添加元素
    list1.append(200)
    print(list1)
    # 指定位置插入元素
    list1.insert(1, 400)
    print(list1)
    # 删除元素
    list1.remove(400)  # 删除指定元素
    print(list1)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]  # 删除指定索引位置元素
    print(list1)
    # 清空列表中的元素
    list1.clear()
    print(list1)


if __name__ == '__main__':
    main()
    pass
