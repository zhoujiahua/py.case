#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    sex: str

    # def __init__(self, name, age, sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex

    def info(self):
        print(self.name)


if __name__ == '__main__':
    s = Student('jerry', 18, 'man')
    print(s.__repr__)
    print(s)
