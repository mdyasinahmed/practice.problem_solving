#include <bits/stdc++.h>
using namespace std;

int main() {
    double N;
    cin >> N;

    int nonFrac = N;
    double frac = N - nonFrac;

    if(frac == 0) {
        cout << "int " << nonFrac;
    } 
    else {
        cout << "float " << nonFrac << " " << fixed << setprecision(3) << frac;
    }

    return 0;
}
