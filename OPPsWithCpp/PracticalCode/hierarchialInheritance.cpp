#include <iostream>

using namespace std;

class Staff
{
protected:
    int code;
    string name;
};

class Teacher : public Staff
{
protected:
    string subject;

    public:
    void read()
    {
        cout << "--------------Staff Detail--------------"<<endl;
        cout << "Enter Staff Code : ";
        cin >> code;
        cout << "Enter Staff Name : ";
        cin >> name;
        cout << "Enter Your Subject : ";
        cin >> subject;
    }
    
    void display()
    {
        cout << "--------------Staff Detail--------------"<<endl;
        cout << "Staff Code : " << code << endl;
        cout << "Staff Name : " << name << endl;
        cout << "Subject Name : " << subject << endl;
    }
};

class Officer : public Staff
{
protected:
    char grade;
    string department;

public:
    void read()
    {
        cout << "Enter Staff Code : ";
        cin >> code;
        cout << "Enter Staff Name : ";
        cin >> name;
        cout << "Enter Your Grade : ";
        cin >> grade;
        cout << "Enter Your Department : ";
        cin >> department;
    }

    void display()
    {
        cout << "--------------Staff Detail--------------"<<endl;
        cout << "Staff Code : " << code << endl;
        cout << "Staff Name : " << name << endl;
        cout << "Grade: " << grade << endl;
        cout << "Department: " << department << endl;
    }
};

class Typist : public Staff
{
protected:
    int speed;
    string experience;
};

class Regular : public Typist
{
protected:
    int salary;

public:
    void read()
    {
        cout << "Enter Staff Code : ";
        cin >> code;
        cout << "Enter Staff Name : ";
        cin >> name;
        cout << "Enter Your Speed : ";
        cin >> speed;
        cout << "Enter Your Expreience : ";
        cin >> experience;
        cout << "Enter Your Salary : ";
        cin >> salary;
    }

    void display()
    {
        cout << "--------------Staff Detail--------------"<<endl;
        cout << "Staff Code : " << code << endl;
        cout << "Staff Name : " << name << endl;
        cout << "Typing Speed : " << speed << endl;
        cout << "Experience : " << experience << endl;
        cout << "Salary : " << salary << endl;
    }
};

class Casual : public Typist
{
protected:
    int dailyWages;

public:
void read()
{
    cout << "Enter Staff Code : ";
    cin >> code;
    cout << "Enter Staff Name : ";
    cin >> name;
    cout << "Enter Your Speed : ";
    cin >> speed;
    cout << "Enter Your Expreience : ";
    cin >> experience;
    cout << "Enter Your Daily Wage : ";
    cin >> dailyWages;
}

void display()
{
    cout << "--------------Staff Detail--------------"<<endl;
    cout << "Staff Code : " << code << endl;
    cout << "Staff Name : " << name << endl;
    cout << "Typing Speed : " << speed << endl;
    cout << "Experience : " << experience << endl;
    cout << "Daily Wage : " << dailyWages << endl;
}
};

int main()
{
    int choice = 0;

    cout << "1.Teacher" << endl;
    cout << "2.Officer" << endl;
    cout << "3.Regular" << endl;
    cout << "4.Casual" << endl;

    cout << "Enter Your Choice : ";
    cin >> choice;

    while (choice < 1 & choice > 4)
    {
        cout << "Enter A Valid Choice Between (1-4) : ";
        cin >> choice;
    }

    Teacher t;
    Officer o;
    Regular r;
    Casual c;

    switch (choice)
    {
    case 1:
        t.read();
        t.display();
        break;
    case 2:
        o.read();
        o.display();
        break;
    case 3:
        r.read();
        r.display();
        break;
    case 4:
        c.read();
        c.display();
        break;

    default:
        break;
    }

    return 0;
}