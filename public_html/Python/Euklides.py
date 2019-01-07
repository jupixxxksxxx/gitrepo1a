#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Euklides.py
#  
#  Copyright 2019  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def nwdv1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def nwdv2(a, b):
    """Wersja optymalna"""
    while a > 0:
        a = a % b
        b = b - a
    return b




def main(args):

    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    print(nwdv2(a, b))








   
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))







































































