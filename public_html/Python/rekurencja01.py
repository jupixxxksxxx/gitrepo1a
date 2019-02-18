#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencja01.py
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

import turtle


def rysuj_it(ile, bok, kat):
    for i in range(ile):
        turtle.forward(bok)
        turtle.right(kat)



def rysuj_rek(ile, bok, kat):
    if ile < 1:
        return
    turtle.forward(bok)
    turtle.right(kat)
    rysuj_rek(ile - 1, bok, kat)
    
    
    
    
    
    
    



def main(args):
    turtle.setup(800, 600)
    rysuj_rek(5, 100, 72)
    
    turtle.done()
    
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))















