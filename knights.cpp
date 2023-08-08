// “Author: Varun Asuri
// It is ok to post my anonymized solution

#include <iostream> // use for cout and cin for input output processing
#include <vector> // use for the 2d array grid of the board of knights

using namespace std;
vector<vector<int>> C { // creating a vector for the solution board to compare with an overloaded ==
    {1, 1, 1, 1, 1},
    {2, 1, 1, 1, 1},
    {2, 2, 0, 1, 1},
    {2, 2, 2, 2, 1},
    {2, 2, 2, 2, 2}
};

int solveBoard(vector<vector<int>> v, int m, int x, int y, int l)
{
    if(v == C) return m; // if this current board is the solution board return the number of moves made
    if(m == 11) return m; // if this has reached 11 moves return 11 to print the error message
    int p = 11, t = 0; // set the base moves to 11 and placeholder value to 0
    if(y > 1 && x > 0 && l != 1) // if i can move up and over to the left and didnt move down and over to the right previously make the move
    {
        v[x][y] = v[x-1][y-2]; // define the blank as what it is going to be
        v[x-1][y-2] = 0; // define the new spot as a blank
        x = x-1; // adjust the x and y spots of the blank based on the move
        y = y-2;
        t = solveBoard(v, m+1, x, y, 4); // call a solve for this specific move on the board
        v[x][y] = v[x+1][y+2]; // undo all the changes based on what move was just made earlier
        v[x+1][y+2] = 0;
        x = x+1;
        y = y+2;
        if(t < p) p = t;
    }
    if(y > 1 && x < 4 && l != 2) // if i can move up and over to the right and didnt move down and over to the left previously make the move
    {
        v[x][y] = v[x+1][y-2];
        v[x+1][y-2] = 0;
        x = x+1;
        y = y-2;
        t = solveBoard(v, m+1, x, y, 3);
        v[x][y] = v[x-1][y+2];
        v[x-1][y+2] = 0;
        x = x-1;
        y = y+2;
        if(t < p) p = t;
    }
    if(y < 3 && x > 0 && l != 3) // if i can move down and over to the left and didnt move up and over to the right previously make the move
    {
        v[x][y] = v[x-1][y+2];
        v[x-1][y+2] = 0;
        x = x-1;
        y = y+2;
        t = solveBoard(v, m+1, x, y, 2);
        v[x][y] = v[x+1][y-2];
        v[x+1][y-2] = 0;
        x = x+1;
        y = y-2;
        if(t < p) p = t;
    }
    if(y < 3 && x < 4 && l != 4) // if i can move down and over to the right and didnt move up and over to the left previously make the move
    {
        v[x][y] = v[x+1][y+2];
        v[x+1][y+2] = 0;
        x = x+1;
        y = y+2;
        t = solveBoard(v, m+1, x, y, 1);
        v[x][y] = v[x-1][y-2];
        v[x-1][y-2] = 0;
        x = x-1;
        y = y-2;
        if(t < p) p = t;
    }
    if(x > 1 && y > 0 && l != 5) // if i can move left and upward and didnt move right and downward previously make the move
    {
        v[x][y] = v[x-2][y-1];
        v[x-2][y-1] = 0;
        x = x-2;
        y = y-1;
        t = solveBoard(v, m+1, x, y, 8);
        v[x][y] = v[x+2][y+1];
        v[x+2][y+1] = 0;
        x = x+2;
        y = y+1;
        if(t < p) p = t;
    }
    if(x > 1 && y < 4 && l != 6) // if i can move left and downward and didnt move right and upward previously make the move
    {
        v[x][y] = v[x-2][y+1];
        v[x-2][y+1] = 0;
        x = x-2;
        y = y+1;
        t = solveBoard(v, m+1, x, y, 7);
        v[x][y] = v[x+2][y-1];
        v[x+2][y-1] = 0;
        x = x+2;
        y = y-1;
        if(t < p) p = t;
    }
    if(x < 3 && y > 0 && l != 7) // if i can move right and upward and didnt move left and downward previously make the move
    {
        v[x][y] = v[x+2][y-1];
        v[x+2][y-1] = 0;
        x = x+2;
        y = y-1;
        t = solveBoard(v, m+1, x, y, 6);
        v[x][y] = v[x-2][y+1];
        v[x-2][y+1] = 0;
        x = x-2;
        y = y+1;
        if(t < p) p = t;
    }
    if(x < 3 && y < 4 && l != 8) // if i can move left and downward and didnt move right and upward previously make the move
    {
        v[x][y] = v[x+2][y+1];
        v[x+2][y+1] = 0;
        x = x+2;
        y = y+1;
        t = solveBoard(v, m+1, x, y, 5);
        v[x][y] = v[x-2][y-1];
        v[x-2][y-1] = 0;
        x = x-2;
        y = y-1;
        if(t < p) p = t;
    }
    return p; // return solution at the end of all the checks even if we didnt get anything
}

int main()
{
    int n, x, y; // define the number of test cases along with the coordinates for the empty square
    cin >> n;
    string line;
    getline(cin, line); // read the next new line character and use this to get each line 

    for(int q = 0; q < n; q++) // loop through the test cases under n
    {
        vector<vector<int>> v // define the 2d array for input processing 
        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}
        };
        for(int i = 0; i < 5; i++)
        {
            getline(cin, line); // get each line in the input
            for(int j = 0; j < 5; j++)
            {
                if(line[j] == '0') v[i][j] = 2; // if this is a white piece use my personal numbering method of 2
                else if(line[j] == '1') v[i][j] = 1; // if this is a black piece use 1
                else // if i found the empty square store it for the recursion part of the problem
                {
                    x = i; 
                    y = j;
                }
            }
        }
        
        int r = solveBoard(v, 0, x, y, 0); // have the first call of recursion on the unchanged board
        if(r == 11) cout << "Unsolvable in less than 11 move(s)." << endl; // if its less than 11 i solved it and output
        else cout << "Solvable in " << r << " move(s)." << endl; // if its not less than 11 i didnt solve
    }

    return EXIT_SUCCESS; // default return for main function
}