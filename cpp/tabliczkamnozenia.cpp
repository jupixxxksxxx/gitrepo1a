/*
 * tabliczkamnozenia.cpp
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

#define N	11

#define M	11


int main(int argc, char **argv) {
	int tab2W[N][M];
	int i, j;
	for (i = 1;i < N; i++) {
		cout << i ;
		for(j = 0; j < M; j++) {
			tab2W[i][j] = i * j;
			cout << setw(4) << tab2W[i][j] << " ";
}
		cout << endl;


}

	return 0;
}

