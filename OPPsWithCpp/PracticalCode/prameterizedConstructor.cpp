#include <iostream>

using namespace std;

class Circle
{
protected:
    double Radius;

public:
    Circle(double r)
    {
        Radius = r;
    }

    void displayCircumference()
    {
        cout << "Circumference Of The Circle Is : " << 2 * 3.14 * Radius<<endl;
    }

    void displayArea()
    {
        cout << "Area Of The Circle Is : " << 3.14 * Radius * Radius<<endl;
    }
};

int main()
{
    int r = 0;
    cout << "Enter The Radius : ";
    cin >> r;

    while (r < 0)
    {
        cout << "Enter A Positive Number : ";
        cin >> r;
    }

    Circle c(r);
    c.displayCircumference();
    c.displayArea();
    return 0;
}