#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    char name[100];
    int size;
    cout << "Enter The Length Of The Name : ";
    cin >> size;
    // User Input
    cout
        << "Enter Name : ";
    for (int i = 0; i < size; i++)
    {
        cin >> name[i];
    }

    cout << "Your Name Is : ";
    for (int i = 0; i < size; i++)
    {
        if (name[i])
        {
            cout << name[i];
        }
        else
        {
            break;
        }
    }

    return 0;
}