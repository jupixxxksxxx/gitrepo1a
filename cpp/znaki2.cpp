/*
 * znaki2.cpp
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
 * Znakiem kończącym tablicę jest \0 (bekslesz zero)
 * 
 */


#include <iostream>

using namespace std;

void ascii() {
    
    int i = 0;
    for (i = 65; i < 91; i++) {
        cout << i << " - " << char(i) << endl;

}    
}

void litery2liczby(char tabzn[], int rozmiar) {
    
    for (int i = 0; i < rozmiar; i++) {
        cout << tabzn[i] << " - " << (int)tabzn[i] << endl;

}
}


int main(int argc, char **argv) {

    int rozmiar = 13;
    char napis[rozmiar] = "Ala ma kota!";
    
    ascii();
    litery2liczby(napis, rozmiar);
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	return 0;
}

