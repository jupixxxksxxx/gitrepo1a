#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
#  
#  Copyright 2018  <>
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
#zdefiniuj klasę samochód z następującymi atrybutami i metodami:
#marka, model, rok produkcji, metoda wiek(), która zwroci wiek samochodu w latach
#
#
#
from datetime import date
from osoba_obj import Osoba

class Kierowca(Osoba):
    
    licznik = 0
    
    def __init__(self, imie, nazwisko, kategoria):
        super().__init__(imie, nazwisko)
        self.kategoria = kategoria
        Kierowca.licznik += 1
        
    def __del__(self):
        Kierowca.licznik -= 1
        
        
    @staticmethod #Metoda Statyczna
    def KierowcaLicz():
        
    
       return KierowcaLicz
    
    
    
        
        
class Samochod:

    def __init__(self, marka, model, rocznik):
        self.marka = marka
        self.model = model
        self.rok = rocznik
        
        
    
        
        
        
    def wiek(self):
        dzis = date.today()
        return dzis.year - self.rok


def main(args):
    c1 = Samochod('Fiat', '126p', '1989')
    c2 = Samochod('Seat', 'leon', '2005')
    c3 = Samochod('Ursus', 'jd', '1922')
    c4 = Samochod('Wolkswagen', 'Touran', '1939')
    
    k1 = Kierowca('Adamus', 'Słodowus', 'B')
    print(k1.imie, k1.nazwisko, k1.kategoria)
    print(c1.marka, c1.model, c1.rok)
    print(k1.licznik)
    
    k2 = Kierowca('Norbert', 'Gierczak', 'JD')
    print(k2.imie, k2.nazwisko, k2.kategoria)
    print(c2.marka, c2.model, c2.rok)
    print(k2.licznik)
    
    k3 = Kierowca('Michałus', 'Rożmiejus', 'C++')
    print(k3.imie, k3.nazwisko, k3.kategoria)
    print(c3.marka, c3.model, c3.rok)
    print(k3.licznik)
    
    del(k2)
    del(k3)
    print(k1.KierowcaLicz())


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))






























