filename = input("open this file , What is filename?")

file = open(filename, 'w')

file.write(input("你想输入什么？"))

file.close()
