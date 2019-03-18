#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wykres01.py
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
import matpolib.pyplot as plt



def main(args):
    # y = a*x + b
    a = int(input('Podaj współczynnik a:'))
    b = int(input('Podaj współczynnik b:'))
    x = range(-10, 11)
    y = [a * i + b for i in x]
    
    plt.plot(x, y)
    plt.title('Wykres f(x,) = {}*x + {}'.format(a,b))
    plt.grid(True)
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
