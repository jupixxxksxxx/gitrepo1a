/*
 * potega.cpp
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

// x0 = 1 dla x=/0
// x1 = x
// xn = x * ... * x(n-czynników)

long int potega_it(float x, int n) {
    
    float potega = 1;
    
    for(int i=0; i < n; i++) {
        
        potega = potega * x;
        
}
        
        return potega;

}

// x0 = 1 dla x=/0
// xn = x(n - 1) * x

float potega_re(float x, int n) {

    if (n==0)

        return 1;

    else

        return potega_re(x, n - 1) * x;
        
}

int main(int argc, char **argv) { 
    
    
    float x;
    int n;
    cout << "Podaj podstawę: " << endl;
    cin >> x;
    cout << "Podaj wykładnik: " << endl;
    cin >> n;
    cout << "Potęga: " << potega_it(x, n);
	return 0;
}

