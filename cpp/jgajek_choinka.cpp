

#include <iostream>

#include <iomanip>

using namespace std;

void choinka(int x, char z, char p) {
    for (int i = 1; i <= x-1; i++) {
        for (int k = 1 ; k <= x-i-1 ; k++) {
            cout << " ";
}
            for (int j = 1; j <= 2*i-1 ; j++) {
                cout << z;
}
        cout << endl;
}

    for (int pien = 1; pien <= x-2; pien++) {
		cout << " ";
}
		cout << p;
}

int main() {
    int x;
    char znak1;
    char znak2;
    cout << "Podaj wysokosc choinki: ";
    cin >> x;
    cout<< "Podaj znak korony: ";
    cin>>znak1;
    cout<< "Podaj znak pniaka: ";
    cin>>znak2;
    choinka(x, znak1, znak2);
    
    
    
    
    
    
    return 0;
}
