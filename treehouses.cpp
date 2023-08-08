// “Author: Varun Asuri
// It is ok to post my anonymized solution

#include <algorithm> // needed for sort
#include <iostream>
#include <vector> // vectors for arraylist implementation in c
#include <cmath>
using namespace std;

const int MAXN = 1003; // establish a large unreasonable size for d so i can define it without consequences
vector<int> d(MAXN, -1); // define d with all negative ones

int recur(int x) {
    if (d[x] == -1) return x; // if there is no parent return x
    d[x] = recur(d[x]); // if it is linked earlier recur more
    return d[x]; // once i find the parent link return
}

int main() {
    ios_base::sync_with_stdio(false); // fast io
    cin.tie(nullptr);

    int n, e, p;
    cin >> n >> e >> p; // read in the three main numbers
    
    vector<pair<double, double>> t(n); // define my vector of treehouses

    for (int i = 0; i < n; i++) {
        double x, y;
        cin >> x >> y;
        t[i] = {x, y}; // read in each treehouse for the vector
    }

    for (int i = 1; i < e; i++) d[i] = 0; // define the first few as 0 to establish that they are connected to the ground and all connected

    for (int i = 0; i < p; i++) { // read in each pre-existing path and join it in
        int x, y;
        cin >> x >> y;
        x = recur(x - 1), y = recur(y - 1); // go to their parent node
        if (x != y) d[x] = y; // join the nodes of x and y as given due the given path between them
    }

    double a = 0.0; // sum which i use to find total cable length
    vector<pair<double, pair<int, int>>> edges; // vector to store all edges
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            double w = sqrt(pow(t[j].first - t[i].first, 2) + pow(t[j].second - t[i].second, 2)); // calculate distance for every possible edge
            edges.push_back({w, {i, j}}); // add it to my list of edges
        }
    }
    sort(edges.begin(), edges.end()); // sort the edges by distance to go through the minimum distance ones first

    for (auto edge : edges) {
        int x = recur(edge.second.first), y = recur(edge.second.second);
        if (x != y) { // if they dont have the same parent node
            d[x] = y; // join them
            a += edge.first; // add this edge to the running sum of cable length
        }
    }

    cout.precision(10); // ten decimals because why not
    cout << fixed << a << endl; // print the answer which is the total summation cable length

    return 0;
}