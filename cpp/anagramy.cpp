/*
 * anagramy.cpp
 * 
 * Copyright 2019  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    
    //n! = 1 * ... * n 
    
    int r = 4;
    char napis[]="krabq";
    int i1, i2, i3, i4, i5;
    i2 = 1; i3 = 2; i4 = 3; i5 = 4;
    for (i1 = 0; i1 < r; i1++ ) {

        for (i2 = 0; i2 < r; i2++) {  
            if (i2 == i1) continue;
            for (i3 = 0; i3 < r; i3++) {
                if (i3 == i2 || i3 == i1) continue;
                for (i4 = 0; i4 < r; i4++) {
                    if (i4 == i1 || i4 == i2 || i4 == i3) continue; 
                    
                        cout << napis[i1] << napis[i2] << napis[i3] << napis[i4] << napis[i5] << endl;

}

}

}

}

	return 0;

}

