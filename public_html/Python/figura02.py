#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figura01.py
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



def main(args):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    for i in range(5):
        turtle.forward(110)
        turtle.right(144)
    for i in range(5):
        turtle.forward(120)
        turtle.right(144)
    for i in range(5):
        turtle.forward(130)
        turtle.right(144)
    for i in range(5):
        turtle.forward(140)
        turtle.right(144)
    for i in range(5):
        turtle.forward(150)
        turtle.right(144)
    
    turtle.done()
    
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
