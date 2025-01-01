#include <iostream>
using namespace std;

// Requirement
// 1. read () : To Accept The Radius From The User.
// 2 compute () : To Calculate The Area
// 3. display () : To Dispaly The Result


// Defining The Class
class Circle
{
public:
    // Attributes
    double radius, circumference, area;

    // Getting The User Variable
    void read()
    {
        cout << "Enter the radius of the circle: ";
        cin >> radius;
    }

    // Computing The Output
    void compute()
    {
        circumference = 2 * 3.14 * radius;
        area = 3.14 * radius * radius;
    }

    // Displaying The Output
    void display()
    {
        cout << "Circumference Of The Circle: " << circumference << endl;
        cout << "Area Of The Circle : " << area << endl;
    }
};

int main()
{
    // Creating An Object
    Circle c;

    // Assigning The Value
    c.read();

    // Computing The Answer
    c.compute();

    // Printing The Answer
    c.display();

    return 0;
}