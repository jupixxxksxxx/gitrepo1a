#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  osoba_obj.py
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

class Osoba:
    """Prosta klasa opisująca osobę"""
    
    def __init__(self, imie, nazwisko, wiek=0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ustawPlec()
        self.wiek = 0
        
        
    def ustawPlec(self):
        if self.imie[-1] == 'a':
            self.plec = 'k'
        else:
            self.plec = 'm'


def main(args):
    o1 = Osoba('Adam', 'Słodowy')
    o1.wiek = 1939
    o2 = Osoba('Ewa', 'Kos')
    o2.wiek = 1922
    
    print(o1.imie, o1.nazwisko, o1.plec, o1.wiek)
    print(o2.imie, o1.nazwisko, o2.plec, o2.wiek)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
