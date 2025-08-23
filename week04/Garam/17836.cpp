#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int R, C, T;
int map[100][100];
bool visited[100][100][2];
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
bool SUPER;

int bfs() {
    queue<vector<int>> q;

    bool super = (map[0][0] == 2);

    q.push({0, 0, super});
    visited[0][0][super] = true;

    int time = 0;

    while (!q.empty() && time <= T) {   
        int q_size = q.size();

        for (int i = 0; i < q_size; i++) {
            vector<int> coord = q.front();
            q.pop();

            bool super = coord[2];

            if (coord[0] == R-1 && coord[1] == C-1) {
                return time;
            }   

            for (int d = 0; d < 4; d++) {
                int nr = coord[0] + dr[d];
                int nc = coord[1] + dc[d];

                if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                    if (super && !visited[nr][nc][1]) {
                        visited[nr][nc][1] = true;
                        q.push({nr, nc, super});
                    } else if (!super && map[nr][nc] == 0 && !visited[nr][nc][0]) {
                        visited[nr][nc][0] = true;
                        q.push({nr, nc, super});
                    } else if (map[nr][nc] == 2) {
                        visited[nr][nc][0] = true;
                        visited[nr][nc][1] = true;
                        q.push({nr, nc, 1});
                    }
                }
            }
        }

        time++;
    }

    return -1;
}

int main() 
{
    cin >> R >> C >> T;
    
    for (int i = 0; i < R ; i++) {
        for (int j = 0; j < C; j++) {
            cin >> map[i][j];
        }
    }

    int ans = bfs();

    if (ans < 0) {
        cout << "Fail" << endl;
    } else {
        cout << ans << endl;
    }

}