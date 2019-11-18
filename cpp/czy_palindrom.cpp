/*
 * czy_palindrom.cpp
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

bool czy_palindrom(char tab[]) {
    int rozmiar = strlen(tab);
    int i = 0;
    for(i = 0; i < rozmiar / 2; i++) {
        if(tab[i] == tab[rozmiar - 1 - i])
            ;
        else
            return false;
    }
    return true;
}

void removeSpaces(char tab1[], char tab2[]) {
    int rozmiar = strlen(tab1);
    int i = 0;
    for(i = 0; i < rozmiar; i++) {
        if (tab1[i] != ' '){
            tab2[i] = tab1[i];
        }
    }
    tab2[i] = '\0';
}
bool czy_palindrom2(char tab[]){
	int rozmiar = strlen(tab);
	for(int i = 0; i < rozmiar/2; i++){
		if(tab[i] == ' ') i++;
		if(tab[i] == tab[rozmiar- 1 - i])
			;
		else
			return false;
			}

		return true;
	}

int main(int argc, char **argv)
{
    // n! = 1 * ... * n
    // n! = (n-1)! * n

    int r = 20;
    char napis1[r];
    char napis2[r];
    cin.getline(napis1, 20);
    removeSpaces(napis1, napis2);

    cout << napis2 << endl;
    cout << strlen(napis2) << endl;

    if (czy_palindrom(napis2)) {
        cout << " to palindrom " << endl;
    } else {
        cout << " to nie palindrom " << endl;
    }


	return 0;
}








