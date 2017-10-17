#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : example_ch01.py
# @Software: PyCharm
__time__ = '2017/10/13 10:01'
__author__ = 'rtz'


def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result


def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base
    return result


def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return result


def convert_dec_to_any_base_rec(number, base):
    convertString = '0123456789ABCDEF'
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) + convertString[number % base]


def test_convert_to_decimal():
    number, base = 1001, 2
    assert (convert_to_decimal(number, base) == 9)


def test_convert_from_decimal():
    number, base = 9, 2
    assert (convert_from_decimal(number, base) == 1001)


def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert (convert_from_decimal_larger_bases(number, base) == '1F')


def test_convert_dec_to_any_base_rec():
    number = 9
    base = 2
    assert (convert_dec_to_any_base_rec(number, base) == '1001')


if __name__ == '__main__':
    test_convert_to_decimal()
    test_convert_from_decimal()
    test_convert_from_decimal_larger_bases()
    test_convert_dec_to_any_base_rec()
