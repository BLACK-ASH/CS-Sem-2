#include <iostream>
using namespace std;
int main()
{
    // IF ELSE
    int a, b, c;
    cout << "Enter No A : ";
    cin >> a;
    cout << "Enter No B : ";
    cin >> b;
    cout << "Enter No C : ";
    cin >> c;

    if (a > b)
    {
        cout << "A Is Greater Than B" << endl;
    }
    else if (a > c)
    {
        cout << "A Is Greater Than C" << endl;
        if (c>b)
        {
            cout << "C IS Grater THan B"<<endl;
        }
        else{
            cout << "C IS Smaller THan B"<<endl;

        }
        
    }
    else
    {
        cout << "A Is Smallest" << endl;
    }

    return 0;
}