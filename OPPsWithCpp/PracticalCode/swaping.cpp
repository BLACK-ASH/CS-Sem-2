#include <iostream>
using namespace std;

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}
int main()
{
    int a, b;
    a = 10;
    b = 20;
    cout << "The Value Of a,b Before Swap : " << a << "," << b << endl;
    swap(a,b);
    cout << "The Value Of a,b After Swap : " << a << "," << b << endl;

    return 0;
}