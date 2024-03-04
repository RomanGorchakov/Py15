#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    fin = input(': ')
    fout = input(': ')
    
    with open(fin, 'r') as f_in, open(fout, 'w') as f_out:
        f_out.write(''.join(f'{i}: {line}' for i, line in enumerate(f_in.readlines(), 1)))