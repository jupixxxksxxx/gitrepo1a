/*
 * jgajek_tab1.cpp
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
#include <iomanip>

using namespace std;


int main(int argc, char **argv) {
    
    int w = 5;
    int suma1=0;
    int suma2=0;
    int j;
    int tab1[w]; 
    int tab2[w]; 
    
    for( j=0; j<w ; j++) {
        cout<<"podaj liczbę z pierwszej serii: ";
        cin >> tab1[j];
}
    for(j=0; j<w ; j++) {
        cout<<"podaj liczbę z drugiej serii: ";
        cin >> tab2[j];
	
}
    for(j= 0; j< w; j++) {
        suma1 +=tab1[j];
}
    for(j= 0; j< w; j++) {
        suma2 +=tab2[j];
}
    if(suma1 > suma2) {
        cout<<"Suma tablicy pierwszej jest większa od sumy tablicy drugiej"<<endl;
}
    else {
        cout<<"Suma tablicy drugiej jest większa od sumy tablicy pierwszej"<<endl;
}    
	return 0;
}

