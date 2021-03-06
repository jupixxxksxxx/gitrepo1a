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
import matplotlib.pyplot as plt
from matplotlib.mlab import frange


def main(args):
    # y = a*x + b
    x = frange(-1, 2, 0.15)
    # f(x) = x / (x+2) dla x >= 1
    # f(x) = x * x/3 dla x > 0 i x <1
    # f(x) = x / -3 dla x <= 0
    y = []
    for el in x:
        if el <= 0:
            y.append(el / -3)
        elif el < 1:
            y.append(el * el / 3)
        else:
            y.append(el / (el + 2))
            
            
    plt.plot(x, y)
    plt.title('Wykres f(x)')
    plt.grid(True)
    plt.show()
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
