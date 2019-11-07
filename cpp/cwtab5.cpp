/*
 * cwtab5.cpp
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
#include <cstring>

using namespace std;

#define rozmiar 100

int main(int argc, char **argv) {
	
    char tekst(rozmiar);
    int i = 0;
    
    cout << "Podaj ciąg znaków: " << endl;;
    cin.getline(tekst, rozmiar);
    
    for (i = 0; i < strlen(tekst); i++) {
        if(tekst[i] > 95) {
        cout << (char(tekst[i] - 32));     
}
    else if(tekst[i] == 32) {
        cout << (char)(napis[i]);
}
}
    
    
    
    
    
    
    
    
    
    
    
    
    
	return 0;
}

