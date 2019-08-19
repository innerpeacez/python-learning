class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s Studing %s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def main():
    innerpeacez = Student('innerpeacez', 18)
    innerpeacez.study('Python')
    innerpeacez.watch_movie()
    pass


if __name__ == '__main__':
    main()
