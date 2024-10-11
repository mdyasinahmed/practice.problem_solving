#include<bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;

    long long arr[n];
    long long minimum = LLONG_MAX;
    long long position = 0;


    for (long long i = 0; i < n; ++i) {
        cin >> arr[i];

        if (arr[i] < minimum) {
            minimum = arr[i];
            position = i;
        }
    }

    cout << minimum << " " << position << endl;

    return 0;
}
