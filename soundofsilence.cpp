#include <iostream> // import io for cout, cin
#include <vector> // import vector to store the sounds
#include <map> // import the map to use the fast max and min access

using namespace std; // import standard namespace
int main() { // main function
    int n, m, c; // define n, m, and c for user input
    cin >> n >> m >> c; // store n, m, and c from user input
    vector<int> v(n); // define a vector of all the sound measurements
    for(int i = 0; i < n; i++) cin >> v[i]; // for every value in the cin add to the vector

    bool p = false; // a boolean to check if i ever printed
    map<int, int> t; // the map which will store quantities of the current window
    for(int i = 0; i < n; i++) { // for every value in the list
        t[v[i]]++; // add this number to the map for the current window
        if(i >= m-1) { // if i have passed m-1 iterations i can start checks
            if(t.rbegin()->first - t.begin()->first <= c) { // if max-min is under or at c
                p = true; // i printed so i store it in the boolean
                cout << i-m+2 << "\n"; // output the current window location
            }
    
            t[v[i-m+1]]--; // remove the last value from the map
            if(t[v[i-m+1]] == 0) t.erase(v[i-m+1]); // erase it from the map if it was the only occurence
        }
    }

    if(!p) cout << "NONE\n"; // if never printed, print none
}