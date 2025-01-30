#include <iostream>
using namespace std;

class Salary
{
protected:
    double salary = 60000;
};

class Programmer : public Salary
{
protected:
    string Name = "John Doe";
    double bonous = 6000;

public:
    void display()
    {
        cout << "My Name Is : " << Name << endl;
        cout << "My Bonous Is : " << bonous << endl;
        cout << "My Salary Is : " << salary << endl;
        cout << "My Gross Salary Is : " << salary + bonous << endl;
    }
};

int main (){
    Programmer p;
    p.display();

    return 0;
}