/*
 * funkcje.cpp
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

void sumuj(int a, int b){
    cout << "Suma: " << a+b << endl;
}

void podziel (int a, int b) {
        if (b != 0)
            cout << "Iloraz: " << (float)a/(float)b << endl;
        else
            cout << "Błąd" << endl;
}

int pomnoz(int a, int b) {
    
    return a*b;
    
}
int odejmij(int a, int b) 
{

    return a-b;

}


int main(int argc, char **argv)
{
    int a, b;
    cout <<"Podaj liczby:"<< endl;
    cin >> a >> b;
     //sumuj(a, b);
	 //podziel(a,b);
     //cout << "Iloczyn: " << pomnoz(a, b) << endl;
     cout << "Roznica: " << odejmij(a, b) << endl;
     int wynik;
     wynik = odejmij(a, b);
     cout << "Róznica: " << wynik;
     //wynik = pomnoz(a,b);
     //cout << "Iloczyn:" << wynik;
     
	return 0;
}

