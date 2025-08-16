#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() 
{
    int N, K;
    cin >> N >> K;

    deque<int> belt;

    for (int i = 0; i < 2 * N; i++) {
        int a;
        cin >> a;
        belt.push_back(a);
    }

    int turn = 1;

    deque<int> robotIdx;

    while (true) {
        // stage 1
        int num = belt.back();
        belt.pop_back();
        belt.push_front(num);

        for (int i = 0; i < robotIdx.size(); i++) {
            robotIdx[i]++;
        }

        if (!robotIdx.empty() && robotIdx.back() == N-1) robotIdx.pop_back();

        // stage 2
        for (int i = robotIdx.size()-1; i >= 0; i--) {
            if (belt[robotIdx[i]+1] > 0) {
                bool occupied = false;
                for (int j = i+1; j < robotIdx.size(); j++) {
                    if (robotIdx[j] == robotIdx[i] + 1) occupied = true;
                }
                if (occupied) continue;
                robotIdx[i]++;
                belt[robotIdx[i]]--;   
            }
        }

        if (!robotIdx.empty() && robotIdx.back() == N-1) robotIdx.pop_back();

        // stage 3
        if (belt.front() != 0) {
            robotIdx.push_front(0);
            belt[0] -= 1;
        }

        // stage 4
        int count = 0;
        for (int i = 0; i < 2 * N; i++) {
            if (belt[i] == 0) count++;
        }

        if (count >= K) {
            cout << turn << endl;
            break;
        }

        turn++;
    }
}