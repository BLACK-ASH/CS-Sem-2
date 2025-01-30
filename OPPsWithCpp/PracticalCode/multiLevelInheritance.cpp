#include <iostream>
using namespace std;

class Data
{
protected:
    double P, C, M, B;

public:
    void read()
    {
        cout << "Enter Physics Marks : ";
        cin >> P;
        cout << "Enter Chemistry Marks : ";
        cin >> C;
        cout << "Enter Maths Marks : ";
        cin >> M;
        cout << "Enter Biology Marks : ";
        cin >> B;
    }
};

class Sum : public Data
{
protected:
    double totalMarks;

public:
    void sum()
    {
        totalMarks = P + C + M + B;
    }
};

class Percent : public Sum
{
protected:
    double totalPercent;

public:
    void calculate()
    {
        totalPercent = (totalMarks / 400) * 100;
    }
    void display()
    {
        cout << "----------Result----------" << endl;
        cout << "Physics : " << P << endl;
        cout << "Chemistry : " << C << endl;
        cout << "Maths : " << M << endl;
        cout << "Biology : " << B << endl;

        cout << "Total Marks : " << totalMarks << endl;
        cout << "Total Percantage : " << totalPercent << endl;
    }
};

int main()
{
    Percent john;
    john.read();
    john.sum();
    john.calculate();
    john.display();

    return 0;
}