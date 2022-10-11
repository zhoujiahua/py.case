#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Person:
    score = 'admin'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def infos(self):
        return {
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
        }


class Student(Person):

    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('Setter value.')

    def info(self):
        self.cls_info()
        self.stc_info()
        print(self.infos())
        print("I am", self.name, "and i am", self.age, "years old", "study", self.score)

    @classmethod
    def cls_info(cls):
        print(f'classmate:{cls.score}')

    @staticmethod
    def stc_info():
        print(f'staticmethod:{Student.score}')


if __name__ == "__main__":
    # p = Person('jerry', 18, 'man')
    # print(p.infos())
    s = Student('jerry', 18, 'man')
    s.info()
