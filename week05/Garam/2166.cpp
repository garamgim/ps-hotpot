#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<pair<double, double>> coords(N + 1);

    for (int i = 0; i < N; i++) {
        double x, y;
        cin >> x >> y;
        coords[i] = {x, y};
    } 

    coords[N] = coords[0];

    double res = 0;

    for (int i = 0; i < N; i++) {
        res += coords[i].first * coords[i+1].second;
        res -= coords[i].second * coords[i+1].first;
    }

    double ans = abs(res) / 2.0;

    cout << fixed << setprecision(1) << ans << endl;
}