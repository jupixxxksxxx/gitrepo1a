#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  palindorm.py
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
import os 

def czy_palindrom(tekst):
    ile = len(tekst)
    for i in range(ile // 2):
        if tekst[i] != tekst[-i-1]:
            return False

    return True
    
def czytaj_dane(plik):
    if not os.path.exists(plik):
        print('Plik niedostępny')
        return False
    teksty = []
    with open(plik, "r") as f:
        for wiersz in f:
            teksty.append(wiersz.strip())
        return teksty

def main(args):
    # tekst = input("podaj tekst ")
    teksty = czytaj_dane('dane01.txt')
    ile = 0
    for i in range (len(teksty)):
        if czy_palindrom(teksty[i]):
            ile += 1

        else:
            continue
    # ~if czy_palindrom(tekst):
        # ~print('to palindrom')
    # ~else:
        # ~print(' to nie palindrom')
    print ("Palindromow jest:")
    print(ile)
    return 0


























if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
