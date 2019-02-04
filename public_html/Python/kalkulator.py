#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py
#  
#  Copyright 2019  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def pokaz_liste():
    print('''Lista działań:
          +  – dodawanie
          -  – odejmowanie
          *  – mnożenie
          /  – dzielenie
          // – dzielenie całkowite
          %  – dzielenie modulo
          ^  – potęgowanie
          !  – silnia
          sin – sinus
          cos – cosinus
          koniec – wyjście z programu
          ''')
          
def pobierz_liczbe(komunikat'Pobierz liczbe:')
    a = input(komunikat)
    if a.isadigit():
        return int.a
        
def dziel(a, b):
    if b != 0:
        return a/b
    else:
        print("Nie dziel przez 0")
    return False


def main(args):
    pokaz_liste()
    while True:
        d = input("Wybierz dzialanie")
        if d == '+':
            pass
        elif d == '-':
            pass
        elif d == '*':
            pass
        elif d == '/':
            a = pobierz_liczbe('Podaj Dzielna')
            b = pobierz_liczbe('Podaj Dzielnik')
            if a and b: 
                wynik = dziel (a, b)
            if wynik:
                print('{} / {} = {} ')
        elif d == '//':
            pass
        elif d == '%':
            pass
        elif d == '^':
            pass
        elif d == '!':
            pass
        elif d == 'sin':
            pass
        elif d == 'cos':
            pass
        elif d == 'l':
            pokaz_liste()
        elif d == 'koniec':
            return 0
        else: print ("Błędny wybór!")
    
    
    
    
    
    
    
    
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
