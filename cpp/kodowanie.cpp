/*
 * kodoj.cpp
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

void koduj(char tabzn[],int rozmiar) {
	
	cout << "Podaj tekst do zakodowania(max "<<rozmiar<< "): ";
	cin >> tabzn;
	for (int i = 0; i< rozmiar; i++) {
		
		cout << (int)tabzn[i]<<" ";
}
}

void litery2liczby (char tabzn[], int rozmiar) {
	
	for(int i =  0; i < rozmiar; i++) {
	cout<< (int)tabzn[i] << endl; 
	
}
}

void dekoduj(int kod[], int rozmiar) {
	
	cout << "Podaj kod do odkodowania(max"<<rozmiar<<" znakow, oddzielone enterami): "<< endl;
	for(int i = 0; i < rozmiar; i++) {
	cin >> kod[i];
	
}

	cout<< "twoj kod to: " << endl; 
	for (int i= 0; i < rozmiar; i++) {
		cout<< (char)kod[i];
		
}
}




 
int main(int argc, char **argv)	{
	
	int rozmiar = 10;
	char napis[rozmiar];
	int kod[rozmiar];
	koduj(napis, rozmiar);
	cout << endl;
	dekoduj(kod, rozmiar);
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}

