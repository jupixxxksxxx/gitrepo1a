#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wykres03.py
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
import numpy as np

def f(a, b, c, x):
    return a * x**2 + b * x + c
    
def rozwiaz(a, b, c):
    delta = b**2 - 4 * a * c
    if delta >0:
        p1 = (-b - np.sqrt(delta)) / 2 *a
        p2 = (-b + np.sqrt(delta)) / 2 *a
        return (p1, p2)
    elif delta == 0:
        p = -b / 2 * a
        return (p, )
    else:
        return None


def rysujFun(a, b, c):
    x = np.linspace(-10, 10, 50)
    y = [f(a, b, c, w) for w in x]
    plt.plot(x, y)
    plt.grid(True)
    plt.show()






def main(args):
    
    a = 0
    while a == 0:
        a = int(input("Podej współczynnik a:"))
    b = int(input("Współczynnik b:"))
    c = int(input("Współczynnik c:"))
    mzerowe = rozwiaz(a, b, c)
    if mzerowe and len(mzerowe) > 1:
        x1, x2 = mzerowe
        print('f({:.2f}) = :{:.2f}, f({:.2f}) = {:.2f}'.format(x1, f(a, b, c, x1), x2, f(a, b, c, x1)))
    elif mzerowe:
        x = mzerowe[0]
        print('f({:.f2}) = {:.f2}'.format(x, f(a, b, c, x)))
    else:
        print('Brak rozwiązań')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))