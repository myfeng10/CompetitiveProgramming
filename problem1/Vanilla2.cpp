#include <iostream>
using namespace std;

int main(){
    int n,k;
    cin >> n >> k;
    int count = 0;
    for (int i=0;i<n;i++){
        int num;
        cin >> num;
        if (num%k==0){
            count++;
        }
    }
    cout << count << endl;
}