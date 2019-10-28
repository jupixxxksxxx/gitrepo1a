/*
 * jgajek_tab4.cpp
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
	
    int tab1[5][7];
    int i, j;
    float r;
    cout << "Podaj wartość powiększenia liczb: ";
    cin >> r;
    float a;
    cout << "Podaj pierwszą wartość: ";
    cin >> a;
    
    for(i = 1; i < 6; i++) {
        for(j = 0; j < 7; j++) {
            tab1[i][j] = a;
            a += r;
            cout << tab1[i][j] << ", ";
            
}

            cout << endl;

}
        
	return 0;
}

