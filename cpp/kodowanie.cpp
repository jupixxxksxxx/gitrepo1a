/*
 * kodowanie.cpp
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

void koduj(char tabzn[], int rozmiar) {

    int i = 0;
    for(i = 0; i < rozmiar; i++) {
        cout << (int)tabzn[i] << " ";
}
}

void dekoduj(char szyfr, int rozmiar) {

    int a = 0;
    int i = 0;
    for(i = 0; i < rozmiar; i++) {
        cout << "Podaj liczbe" << endl;
        cin >> a;
        
}    
}

int main(int argc, char **argv) {
    
    int rozmiar = 19;
    
    char napis[rozmiar] = "janooshvietchowreck";
    
    koduj(napis, rozmiar);
    
    int szyfr[19] = {106 97 110 111 111 115 104 118 105 101 116 99 104 111 119 114 101 99 107 };
    //dokoduj(szyfr, rozmiar);
	
    
    
    
    
    
    
    
    
    
    
    
	return 0;
}

