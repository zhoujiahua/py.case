#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def get_day_name(day):
    def get_sunday():
        return 'Sunday'

    def get_monday():
        return 'Monday'

    def get_tuesday():
        return 'Tuesday'

    def get_default():
        return 'Unknown'

    switcher = {
        0: get_sunday,
        1: get_monday,
        2: get_tuesday
    }

    return switcher.get(day, get_default)()


if __name__ == '__main__':
    print(get_day_name(2))
