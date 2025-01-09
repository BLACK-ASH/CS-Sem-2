#include <iostream>

using namespace std;

class Sum
{
public:
    // Declaring Variable
    int num, sum =0, squareSum =0 ;

    void read()
    {
        cout << "Enter A Number : ";
        cin >> num;
    }

    // Taking User Input
    void calculate()
    {
        for (int i = 1; i <= num; i++)
        {
            squareSum += i * i;
        }
        for (int i = 1; i <= num; i++)
        {
            sum += i;
        }
    }

    // Displaying The Values
    void display()
    {
        cout << "Sum Of Number Till " << num << " Is : " << sum << endl;
        cout << "Sum Of Square Of Number Till " << num << " Is : " << squareSum << endl;
    }
};

int main()
{
    // Creating Object
    Sum sum;
    sum.read();
    sum.calculate();
    sum.display();
    return 0;
}