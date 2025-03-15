#include <iostream>;
#include <fstream>;

using namespace std;

int main()
{
    string letter;
    char ch;
    ofstream small("small.txt");
    ofstream capital("capital.txt");
    int count = 1;

    // File 1
    ifstream MyReadFile1("input.txt");
    while (getline(MyReadFile1, letter))
    {
        if (count <= 5)
        {
            small << letter << "\n";
        }
        else
        {
            capital << letter << "\n";
        }
        count ++;
    }
    MyReadFile1.close();

    // Concating File
    small.close();
    capital.close();
    cout << "New File Created ";
    return 0;
}