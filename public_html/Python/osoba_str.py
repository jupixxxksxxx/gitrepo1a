#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  osoba_str.py
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

def zapisz_dane(imie, nazwisko):
    osoba = [imie, nazwisko]
    return osoba
    
def zapisz_dane2(imie, nazwisko):
    osoba = {'imie': imie, 'nazwisko': nazwisko}
    return osoba



def main(args):
    ol = zapisz_dane('Adam', 'Słodowy')
    print (o1[0], o1[1])
    
    o2 = zapisz_dane2('Ewa', 'Kos')
    print(o2['imie'], o2['Nazwisko'])
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
