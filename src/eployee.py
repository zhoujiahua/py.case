#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Employee:
    __version = '1.0.0'

    def __init__(self, name, age):
        self.__money = 0
        self.__dep = 1
        self.name = name
        self.age = age

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('Setter money value error.')


if __name__ == '__main__':
    em = Employee('jerry', 18)
    em.money = 1000
