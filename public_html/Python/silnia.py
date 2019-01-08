#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
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

# n! = 1 dla n = 0
# n! = n * (n-1)! dla n >= 1
# n! = 1 * ... * n
# 4! = 1 * 2 * 3 * 4







def main(args):
    n=int(input("Podaj liczbę naturalną:"))
    wynik = 1
    for i in range(1, n + 1):
        wynik = wynik * i
    print (wynik)
    
    
    
    
    
    
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
