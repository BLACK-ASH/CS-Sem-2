#include <iostream>

using namespace std;

class Student
{
protected:
    string Name, Stream;
    int Age, RollNo;

public:
    Student()
    {
        cout << "Enter Your Name : ";
        cin >> Name;
        cout << "Enter Your Stream : ";
        cin >> Stream;
        cout << "Enter Your Age : ";
        cin >> Age;
        cout << "Enter Your Roll No : ";
        cin >> RollNo;
    }

    void display()
    {
        cout << "Name : " << Name << endl;
        cout << "Stream : " << Stream << endl;
        cout << "Age : " << Age << endl;
        cout << "Roll No : " << RollNo << endl;
    }
};

int main()
{
    Student s;
    s.display();

    return 0;
}