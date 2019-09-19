/*
 * trojkat.cpp
 * 
 * Napisz program, który pobiera od użytkownika trzy liczny,
 * długość boków i sprawdza, czy da się z nich zbudować trójkąt,
 * Program powinien wyprowadzić odpowiedni komunikat.
 * Jeśli da się zbudować trójkąt, to sprawdź czy to trójkąt prostokątny.
 * Wyprowadź odpowiedni komunikat
 * 
 */


#include <iostream>
using namespace std;
int bok1;
int bok2;
int bok3;

int main(int argc, char **argv)
{
	cout<<"Podaj pierwszy bok:";
    cin>>bok1;
    cout<<"Podaj drugi bok:";
    cin>>bok2;
    cout<<"Podaj trzeci bok:";
    cin>>bok3;
    
    if (bok1 + bok2 > bok3) {
        if(bok1 + bok3 > bok3) {
            if(bok2 + bok3 > bok1) {
                cout<<"Trójkąt o bokach bok1 bok2 bok3 istnieje";}
            else{
                cout<<"Taki trójkąt nie istnieje";}

        else{
                cout<<"Taki trójkąt nie istnieje";}}

    else{
                cout<<"Taki trójkąt nie istnieje";}}


    
    
    
    

    
	return 0;
}

