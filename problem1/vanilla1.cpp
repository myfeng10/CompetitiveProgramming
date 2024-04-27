#include <iostream>
using namespace std;

int main(){
    int num;
    cin >> num;
    int a,b,c;
    for (int i = 0; i < num; i++){
        cin >> a >> b >> c;
        if (a != b && a != c){
            cout << a << endl;
        }
        else if (b != a && b!=c){
            cout << b << endl;
        }
        else{
            cout << c << endl;
        } 
    }
}