#include <iostream>;
#include <fstream>;
using namespace std;
int main()
{
    string file1, file2;
    ofstream concatFile("concat.txt");
    // File 1
    ifstream MyReadFile1("test0.txt");
    while (getline(MyReadFile1, file1))
    {
        concatFile << file1 << "\n";
    }
    MyReadFile1.close();
    // File 2
    ifstream MyReadFile2("test1.txt");
    while (getline(MyReadFile2, file2))
    {
        concatFile << file2 << "\n";
    }
    MyReadFile2.close();
    // Concatinf File
    concatFile.close();
    cout << "New File Created ";
    return 0;
}