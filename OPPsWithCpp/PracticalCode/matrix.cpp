#include <iostream>

using namespace std;

int main()
{
    int row = 2, col = 2;
    int matrix[row][col];

    // Input
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << "Enter Element At " << "a" << i + 1 << j + 1 << " : ";
            cin >> matrix[i][j];
        }
    }
    // Display
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
