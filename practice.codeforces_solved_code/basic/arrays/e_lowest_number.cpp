#include<bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;

    long long arr[n];
    long long min_value = LLONG_MAX;  // Initialize to a large value
    long long min_pos = 0;

    // Read the array and find the minimum value and its position
    for (long long i = 0; i < n; ++i) {
        cin >> arr[i];

        if (arr[i] < min_value) {
            min_value = arr[i];
            min_pos = i;
        }
    }

    // Output the minimum value and its position
    cout << min_value << " " << min_pos << endl;

    return 0;
}
