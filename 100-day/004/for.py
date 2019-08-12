sum_number = 0

"""
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
"""

for num in range(101):
    sum_number += num

print(sum_number)
