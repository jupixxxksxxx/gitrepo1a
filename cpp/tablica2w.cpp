/*
 * tablica2w.cpp
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

#define N   3
#define M   3

int main(int argc, char **argv) {
    
    int tab2w[N][M];
    int i, j;
	
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    
    for (i = 0; i < N; i++) {
        // coutniechcemisiępisać
        for (j = 0; j < M; j++) {
            cout << i << " - " << j << endl;
            tab2w[i][j] = rand() % 10;
            cout << tab2w[i][j] << endl;
}       
}    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	return 0;
}

