#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  struktury.py
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

def kolejka():
    from collections import deque
    kolejka = deque([])
    def push(el):
         kolejka.append(el)

    def pop():
        if len(kolejka):
            return kolejka.popleft()
        else:
            print("Błąd Kolejki")
            return None

    push(5)
    push(4)
    print(pop())
    print(pop())
    print(pop())
  









def stos():
    stos = []
    
    def push(el):
        stos.append(el)
    def pop():
        if len(stos):
            return stos.pop()
        else:
            print("Błąd Stosu")
            return None
    push(5)
    push(4)
    
    print(pop())
    print(pop())    
    print(pop())


def main(args):
    kolejka()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
