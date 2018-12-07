#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos.py
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

stos = []
SP = 0 #stack pointer


def push(rozmiar, dane):
    global SP, stos
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1
    else:
        print("Stack overflow!")
        
def pop(rozmiar):
    global SP, stos
    SP -= 1
    if SP  < rozmiar:
        print(stos[SP])
    else:
        print("Stack overflow")
     

def main(args):
    global SP, stos
    rozmiar = 5
    stos = [None] * rozmiar
    push(rozmiar, 2)
    push(rozmiar, 3)
    push(rozmiar, 4)
    push(rozmiar, 5)
    push(rozmiar, 7)
    

    print("Wskaźnik:", SP)
    pop(rozmiar)
    pop(rozmiar)
    pop(rozmiar)



    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
