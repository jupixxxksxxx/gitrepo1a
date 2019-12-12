/*
 * sortowanie.cpp
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

void wypelnij(int tab[], int n) {

    srand(time(NULL));
    for (int i = 0; i < n; i++) {

            tab[i] = rand() % n;

}

}

void wyswietl(int tab[], int n) {

for (int i = 0; i < n; i++) {

    cout << tab[i] << " ";

}

    cout << endl;

}

void copytab(int tab[], int tab2[], int n) {

    for (int i = 0; i < n; i++) {
        tab2[i] = tab[i];
}
    
}

void zamien(int &a, int &b) {

    int tmp = a;
    a = b;
    b = tmp;
    
}

void selection_sort(int tab[], int n) {

    int i, j, k;
    for(i = 0; i < n; i++) {
        
        k = i;
        for (j = i + 1; j < n; j++) {
            if (tab[j] < tab[k])
                k = j;
}
 
    zamien(tab[k], tab[i]);
   
}
 
}

void insert_sort(int, tab[], int n) {

    int i, k, el;
    for(i = 1; i < n; i++) {
        el = tab[i];
        k = i - 1;
        while (k >= 0 && tab[k] < el) {
            tab[k+1] = tab[k];
            k--;
}

        tab[k + 1] = el;

}
    
}


int main(int argc, char **argv) {

    int tab[50];
    int tab2[50];
    int n;
    
    cout << "Ile elementów ma zawierać tablica? (max 50) ";
    cin >> n;
    wypelnij(tab, n);
    copytab(tab, tab2, n);
    wyswietl(tab2, n);


	
	return 0;
}

