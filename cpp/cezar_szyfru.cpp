/*
 * cezar_szyfru.cpp
 * 
 * Copyright 2020  <>
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
#include <limits>
#include <string>

using namespace std;

void male_litery(char t[]) {

    int i = 0;
    while (t[i] != '\0') {

        if ((int) t[i] > 64 || (int)t[i] < 91) {
                
            t[i] = (char)((int)t[i] + 32);  

}
            i++;
}

}

void szyfruj(char t[], int k) {
    
    int i = 0;
    int kod = 0;
    while (t[i] != '\0') {

        kod = (int)t[i] + k;
        t[i] = (char)kod;
        i++;
        
}

}

void deszyfruj( char t[], int k) {
    
    int i = 0;
    int kod = 0;
    while (t[i] != '\0') {

        kod = (int)t[i] - k;
        if (kod < 97) {
            
}
        t[i] = (char)kod;
        i++;  
        
}

}


int main(int argc, char **argv) {
    
    int r = 20;
    char tekst[r];
    cout << "Podaj tekst do zamiany" << endl;
    cin.getline(tekst, r); 
    male_litery(tekst);
    int klucz =0;
    cout << "Podaj klucz: " << endl;
    cin >> klucz;
    klucz =  klucz % 26;
    szyfruj(tekst, klucz);
    cout << tekst << endl;
    deszyfruj(tekst, klucz);
    cout << tekst << endl;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	
	return 0;
}

