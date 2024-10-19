#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> fib(51);
    fib[1] = 0;
    fib[2] = 1;
    
    for (int i = 3; i <= 50; ++i) {
        fib[i] = fib[i-1] + fib[i-2];
    }
    
    cout << fib[n] << endl;

    return 0;
}
