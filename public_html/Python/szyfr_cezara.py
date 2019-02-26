#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szyfr_cezara.py
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

def pobierz_klucz():
    try:
        klucz = int(input('Podaj klucz:\n'))
        return klucz % 26
    except ValueError:
        print('Błędny klucz!')
        return 3


def szyfruj_1(tekst, klucz):
    szyfrogram = ' '
    for znak in tekst:
        ascii = ord(znak)
        if ascii + klucz > 122:
            znak = chr(ascii + klucz - 26)
        else:
            znak = chr(ascii + klucz)
            
            
            
        szyfrogram += chr(ascii + klucz)
    print('Szyfrogram:\n', szyfrogram)



def main(args):
    tekst = input('podaj tekst:\n').lower()
    klucz = pobierz_klucz()
    
    szyfruj_1(tekst, klucz)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
