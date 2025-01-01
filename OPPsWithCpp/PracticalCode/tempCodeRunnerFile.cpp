#include <iostream>

using namespace std;

int main()
{
    int sum;
    for (int i = 1; i <= 10; i++)
    {
        cout << i << endl;
        sum = sum + i;
        // cout << sum;
    }
    cout << sum;
    return 0;
}