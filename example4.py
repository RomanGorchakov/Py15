#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    fileptr = open("file2.txt", "r")

    content = fileptr.readlines()

    print(content)

    fileptr.close()