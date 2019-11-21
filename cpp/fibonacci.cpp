/*
 * fibonacci.cpp
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

int fibonacci_it(int n) {
    
    int a = 0;  //Fn-1
    int b = 1;  //Fn-2
    int wynik = 0;
    if (n == 0) return 0;
    if (n == 1) return 1;
    for (int i = 2; i < n; i++) {
        wynik = a + b;
        cout << i << ": fib(" << b << ", " << a << ") = " << wynik << endl;
        b = a;
        a = wynik;    
}

    return wynik;

}

int main(int argc, char **argv) {
    
    //for (int i = 0; i < 20; i++) {
    
    fibonacci_it(999999999);
    //}
	
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	return 0;
}

