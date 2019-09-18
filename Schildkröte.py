#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Schildkröte.py
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
    xd=220
    turtle.speed(500)
    
    turtle.width(15)
    turtle.setup(800, 600)
    turtle.right(45)
    
    for y in range(4):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    
    turtle.right(135)
    turtle.up()
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(220)
    turtle.left(90)
    turtle.down()
    turtle.color("red")
    turtle.width(50)
    for i in range(20):
        turtle.circle(xd)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        xd = xd+40
    
    
    
    
    
   
    
    turtle.done()
    
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
