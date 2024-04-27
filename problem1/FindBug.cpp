#include <iostream>
#include <cmath> 

using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t-->0)
    {
        int n;
        cin >> n;

        double sum = 0.0;
        for(int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            sum += x;
        }
        double sqrtSum = sqrt(sum);
        if(sqrtSum == floor(sqrtSum)) cout << "YES\n";
        else cout << "NO\n";
    }
}