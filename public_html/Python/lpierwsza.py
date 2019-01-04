#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lpierwsza.py
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

def liczbosz():
    n=int(input("Podaj liczbe, którą chcesz sprawdzić:"))
    i = 2
    while i*i<=n:
        if not i==0:
            i=+1
        if i==0:
            print("Liczba złożona")
    if not i*i<=n:
        print("liczba pierwsza")
    if not n%1
            


def main(args):
    liczbosz()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
