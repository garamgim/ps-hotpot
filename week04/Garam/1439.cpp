#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() 
{
    vector<int> v(2, 0);
    string s;
    cin >> s;
    char curr = s[0];
    v[curr - '0']++;

    int count = 0;
    for (int i = 1; i < s.size(); i++) {
        if (s[i] != s[i-1]) {
            curr = s[i];
            v[curr - '0']++;
        }
    }
    if (v[0] < v[1]) {
        cout << v[0] << endl;
    } else {
        cout << v[1] << endl;
    }
}