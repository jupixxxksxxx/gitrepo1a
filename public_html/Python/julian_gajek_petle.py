#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  julian_gajek_petle.py
#  
#  Copyright 2018  <>
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

    
def zad1():
    suma=0
    while suma<75:
        a=int(input("podaj sumowaną liczbę"))
        suma+=a
    print(suma)


def zad2():
    n=int(input("podaj najmniejszą liczbę dodatnią z przedziału licb całkowitych"))
    if n>0:
        m=int(input("podaj największą liczbę całkowitą z przedziału"))
        if m>n:
            for i in range(n,m+1):
                print(" ,", i)
    else:
        print("ERROR")
def zad3():
    m=int(input("podaj największą liczbę całkowitą"))
    for i in range(0,m+1):
        print(i**2)
def zad4_concept1():
    for i in range(1,9):
        for j in range(0,9):
            if not j%2:
                if not j%3 and not i%3:
                    print(i,j)
def zad4():
    print("zad4")
    for i in range(10,99,2):
        if not i%3:
            print(i)
zad1()
zad2()
zad3()
zad4()

def main(args):
    zad1()
    zad2()
    zad3()
    zad4()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
