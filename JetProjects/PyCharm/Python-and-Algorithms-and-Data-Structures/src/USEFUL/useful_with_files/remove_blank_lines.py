#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "bt3"

import sys


def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename)
        for line in fh:
            if line.strip():  # ''也能被append
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if fh is not None:  # AttributeError: 'NoneType' object has no attribute 'close'
            fh.close()
        return lines


def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w")
        for line in lines:
            fh.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()


def remove_blank_lines():
    """
    read a list of filenames on the command line and for each one produces
    another file with the same content but with no blank lines
    """
    if len(sys.argv) < 2:
        print("Usage: remove_blank_lines.py infile1 [infile2...]")

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)


if __name__ == '__main__':
    remove_blank_lines()
