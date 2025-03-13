#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    char msg[20];
    ofstream o;
    o.open("create.txt", ios::out);
    o << "Hello friends !!" << endl;
    o << "bye!!" << endl;
    o.close();
    cout << "New File Created" << endl;

    ifstream i;
    i.open("create.txt", ios::in);
    i >> msg;
    cout << msg << endl;
    i >> msg;
    cout << msg << endl;
    i >> msg;
    cout << msg << endl;
    return 0;
}