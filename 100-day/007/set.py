def main():
    # py 中的集合（set） ,不允许有重复元素，可以进行交集，并集，差集等运算
    set1 = {1, 2, 3, 3, 3, 4, 5, 5, 6}
    print(set1)
    set2 = set(range(1, 10))
    print(set2)
    set1.add(1)
    set1.add(7)
    print(set1)
    set2.update([3, 4])
    set2.update([11, 12])
    print(set2)
    # 删除集合中元素
    set2.discard(5)
    # 删除不存在的元素会抛出异常
    # set2.remove(5)
    print(set2)

    pass


if __name__ == '__main__':
    main()
