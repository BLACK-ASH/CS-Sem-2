#include <iostream>

using namespace std;

int main()
{
    // Initializing The Input Variable
    int n;

    // Staring The Program
    cout << "-----------------START------------------" << endl;
    cout << "Enter A Number For Table : ";

    // Taking User Input
    cin >> n;

    // Printing The Table
    for (int i = 1; i <= 10; i++)
    {
        cout << n << " X " << i << " = " << n * i << endl;
    }

    // End Of THe Program
    cout << "-------------------END------------------" << endl;

    return 0;
}