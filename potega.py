#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
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
#
#
#

def czy_naturalna(a):
    if a.isdigit():
        return True
    return False
    
def potega_it(a, n):
    wynik = 1
    for i in range( n ):
        wynik = a * wynik
    return wynik
    
# a^n = a^(n - 1) * a

def potega_rek(a, n):
    if n == 0
        return 1
    if n == 1
        return a 
    
    


def main(args):
    
    assert potega_rek(2, 0) == 1
    assert potega_rek(2, 1) == 2
    assert potega_rek(0, 10) == 0
    assert potega_rek(1, 10) == 1
    assert potega_rek(3, 3) == 27
    
    
    
    
    a = input("Podaj podstawę:")
    n = input("Podaj wykładnik:")
    if not czy_naturalna(a) or not czy_naturalna(n):
        print("Błędne dane!")
        return 0
    print("{} do potęgi {} = {}".format(a, n, potega_it(int(a), int(n))))
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
