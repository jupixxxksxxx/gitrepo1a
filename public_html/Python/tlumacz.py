#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tlumacz.py
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

from random import randint
import os
import json

def pokaz_menu():
    """Funkcja wyświetla działania dostępne dla użytkownia"""
    print("""
    Wybierz działanie:

    1. Lista słów
    2. Wprowadzanie / edycja słów
    3. Tłumaczenie
    4. Zmień język
    5. Koniec
""")


def listaSlow(dane):
    if not dane:
        print('Brak słow...')
        return
    i = 1
    print()
    for slowo, znaczenia in dane.items():
        print('{}, {}: {}'.format(i, slowo, ','.join(dane[slowo])))
        i += 1


def pobierzZnaczenia():
    znaczenia = input('Podaj znaczenia(a) oddzielone przecinkamie:\n')
    znaczenia = znaczenia.split(',')
    znaczenia = [z.strip() for z in znaczenia]
    return znaczenia








def pobierzDane(dane):
    slowo = input('Podaj Słowo:' ).strip()
    if slowo in dane.keys():
        print('Słowo w bazie.')
        print('{}: {}'.format(slowo, ','.join(dane[slowo])))
        if input('Czy chcesz zmienić znaczneia (t/n)?').lower() == 't':
            dane[slowo] = pobierzZnaczenia()
        else:
            dane[slowo] = pobierzZnaczenia()
            
def tlumacz(dane):
    if not dane:
        print('Brak słow...')
        return
    slowa = list(dane.keys())
    op = 't'
    while op == 't':
        
        slowo = slowa[randint(0, len(slowa) - 1 )]
        print('Przetłumacz:', slowo)
        znaczenia = pobierzZnaczenia()
        poprawne = [z for z in znaczenia if z in dane[slowo]]
        if poprawne:
            print('Poprawne:' , ' , '.join(poprawne))
            slowa.remove(slowo)
        else:
            print('Brak poprawnych znaczeń. Dzbanie')
        if slowa:
            op = input('Następne? (t/n)?').lower()
        else:
            print('Przetłumaczyłeś wszystko!')
            return




def wczytaj_dane(plik, roz='.dat'):
    dane = {}
    if os.path.isfile(plik + roz):
        with open(plik + roz, "r") as f:
            dane = json.load(f)
    else:   
        print('Plik {} nie istnieje.'.format(plik + roz))
    return dane

def wybierzJezyk(konf_dane):
    if konf_dane['jezyki']:
        print('Wybierz język: ')
        for i, j in enumerate(konf_dane['jezyki']):
            print('{}. {}'.format(i + 1, j))
        print('{}. nowy język'.format(i + 2))







            
            
            
            
def main(args):
    #dane ={'go' : ['iść', 'jeździć'], 'see': ['widzieć', 'oglądać']}
    
    konf_plik = 'baza'
    konf_dane = wczytaj_dane(konf_plik)
    if 'jezyki' not in konf_dane:
        konf_dane['jezyki'] = []
        jezyk =
    print(konf_dane)
    return
    
    
    
    
    operacja = 0
    while operacja != 5:
        pokaz_menu()
        operacja = int(input(""))
        if operacja == 1:
            listaSlow(dane)
        elif operacja == 2:
            pobierzDane(dane)
        elif operacja == 3:
            tlumacz(dane)
            
        elif operacja == 5:
            print('CY@')
        else:
            
            print('Błędny wybór')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))























