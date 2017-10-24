#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "bt3"

import collections
import string
import sys


def count_unique_word_file():
    if len(sys.argv) < 2:
        print('Usage: python count_unique_words_files.py FILENAME')

    words = collections.defaultdict(int)
    strip = string.whitespace + string.punctuation + string.digits + "\"'"

    for filename in sys.argv[1:]:
        with open(filename) as file:
            for line in file:
                # if not isinstance(line, unicode):  # 默认编码是ascii
                #     line = line.decode('utf-8').encode('utf-8')
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word) > 2:
                        words[word] = +1

    for word in sorted(words):
        print("'{0}' occurs {1} times.".format(word, words[word]))


if __name__ == '__main__':
    print('sys default encoding is {}'.format(sys.getdefaultencoding()))
    count_unique_word_file()
