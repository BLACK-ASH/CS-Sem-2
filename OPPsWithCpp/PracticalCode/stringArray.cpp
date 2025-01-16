#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    char name[100];

    cout << "Enter Your Name : ";
    gets(name);

    cout << "Your Name Is : " << name;
    
    return 0;
}