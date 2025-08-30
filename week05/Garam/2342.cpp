#include<bits/stdc++.h>
 
using namespace std;
 
const int INF = 0x3f3f3f3f;
int dp[100001][5][5];
vector<int> input;
 
int move(int from, int to) {
    if(from == 0) return 2;
    if(from == to) return 1;
    if(from%2 == to%2) return 4;
    return 3;
}
 
int solve(int idx, int left, int right) {
    if(idx == input.size()) return 0;
    
    int &ret = dp[idx][left][right];
    if(ret != -1) return ret;
    ret = INF;
    
    
    int leftMove = solve(idx+1, input[idx], right) + move(left, input[idx]);
    int rightMove = solve(idx+1, left, input[idx]) + move(right, input[idx]);
    
    ret = min(leftMove, rightMove);
    
    return ret;
}
 
int main() {
    memset(dp, -1, sizeof(dp));
    
    while(true) {
        int a;
        cin >> a;
        if(a == 0) break;
        input.push_back(a);
    }
    
    cout << solve(0, 0, 0);
}