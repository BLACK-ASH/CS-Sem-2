#include <iostream>

using namespace std;

int main()
{
    // Declaring Variable
    int num[5];
    int size = 5;

    // Taking User Input
    for (int i = 0; i < size; i++)
    {
        cout << "Enter Number At Index " << i << ": ";
        cin >> num[i];
    }

    // Printing The Array
    cout << "Elements Of Array : ";
    for (int i = 0; i < size; i++)
    {
        cout << num[i] << " ";
    }

    return 0;
}