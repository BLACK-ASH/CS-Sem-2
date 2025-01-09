#include <iostream>

using namespace std;

int main()
{
    int day = 1;
    cout << "Enter A Number In Between (1-7) To Get Day : ";
    cin >> day;

    while (day > 7 & day < 0)
    {
        cout << "Invalid Input Please Enter A Number In Between (1-7) To Get Day : " ;
        cin >> day;
                  
    }

    switch (day)
    {
    case 1:
        cout << "Monday";
        break;
    case 2:
        cout << "Tuesday";
        break;
    case 3:
        cout << "Wednessday";
        break;
    case 4:
        cout << "Thursday";
        break;
    case 5:
        cout << "Friday";
        break;
    case 6:
        cout << "Saturday";
        break;
    case 7:
        cout << "Sunday";
        break;
    default:
        break;
    }
    return 0;
}