#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        int N;
        cin >> N;
        vector<int> A(N);
        
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        
        int res_min = INT_MAX;

        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                int res = A[i] + A[j] + (j - i);
                res_min = min(res_min, res);
            }
        }
        
        cout << res_min << endl;
    }
    
    return 0;
}
