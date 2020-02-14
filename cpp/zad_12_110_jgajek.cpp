/*
 * zad_12_110_jgajek.cpp
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
#include <cstdlib>

using namespace std;

void sort_b(int tab[],int n) {
    
	for(int i = 0; i < n; i++)
		for(int j = 1; j < n - i; j++)
		if(tab[j - 1] > tab[j])
			
			swap(tab[j - 1], tab[j]);
}

void dzielnik(int d) {

    for(int i = 0; i < d) {
        
        

}
    
}


int main() {
	
    int c;
    cout << "Podaj liczbę całkowitą: " << endl;
    cin >> c >> endl;






















    
  
  return 0;
  
}

