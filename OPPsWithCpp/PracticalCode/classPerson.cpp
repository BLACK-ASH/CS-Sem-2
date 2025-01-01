#include <iostream>

using namespace std;

// Defining The Class
class Person
{
public:
// Attributes
    string name;
    int age;

// Methods
    void introduce()
    {
        cout << "Hello, my name is " << name << " and I am " << age << " years old" << endl;
    }
};

int main()
{
    // Creating An Object
    Person person;

    // Assigning The Value
    person.name = "John Doe";
    person.age = 30;

    // Using Class Methods
    person.introduce();

    return 0;
}
