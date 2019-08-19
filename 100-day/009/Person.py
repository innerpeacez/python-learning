class Person(object):
    def __init__(self, name, age):
        self._name = str(name)
        self._age = int(age)

    __slots__ = ('_name', '_age', '_gender')

    # getter and setter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age


def main():
    person = Person('innerpeacez', 18)
    print(person.name)
    print(person.age)
    person.age = 20
    print(person.age)
    person._gender = 0
    print(person._gender)
    pass


if __name__ == '__main__':
    main()
