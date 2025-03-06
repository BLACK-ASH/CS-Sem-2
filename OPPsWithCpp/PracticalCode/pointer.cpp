#include <iostream>
using namespace std;

int main()
{
    int num, *pNum;
    num = 10;
    pNum = &num;
    cout << "The Value Of num : " << num << endl;
    cout << "Ponter Of num : " << pNum << endl;
    cout << "Value From Pointer Of num : " << *pNum << endl;

    return 0;
}