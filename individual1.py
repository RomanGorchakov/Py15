#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    fileptr = open("harrypotter.txt")
    
    a = fileptr.readlines()
    string = ''
    for el in a:
        string += el
    
    wordStart = 'aeiouy'
    words = string.split()
    for word in words:
        if word[0] in wordStart:
            print(word, sep = " ")