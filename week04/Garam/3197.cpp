
#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int R, C;
char pond[1500][1500];
bool visited[1500][1500];
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
bool FOUND;
queue<pair<int,int>> sq, wq, next_sq, next_wq;

void swan_bfs() {
    while (!sq.empty() && !FOUND) {
        pair<int, int> coord = sq.front();
        sq.pop();

        for (int d = 0; d < 4; d++) {
            int nr = coord.first + dr[d];
            int nc = coord.second + dc[d];

            if (0 <= nr && nr < R && 0 <= nc && nc < C && !visited[nr][nc]) {
                if (pond[nr][nc] == '.') {
                    visited[nr][nc] = true;
                    sq.push({nr, nc});
                } else if (pond[nr][nc] == 'X') {
                    visited[nr][nc] = true;
                    next_sq.push({nr, nc});
                    pond[nr][nc] = '.';
                } else {
                    FOUND = true;
                    return;
                }
            }
        }
    }
}

// 나중에 백조가 가야하니까 방문체크하면 안됨
void water_bfs() {
    while (!wq.empty()) {
        pair<int, int> coord = wq.front();
        wq.pop();

        for (int d = 0; d < 4; d++) {
            int nr = coord.first + dr[d];
            int nc = coord.second + dc[d];

            if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                if (pond[nr][nc] == 'X') {
                    pond[nr][nc] = '.';
                    next_wq.push({nr, nc});
                }
            }
        }
    }
}


int main() 
{
    cin >> R >> C;
    
    for (int i = 0; i < R ; i++) {
        for (int j = 0; j < C; j++) {
            cin >> pond[i][j];
            if (pond[i][j] != 'X') {
                wq.push({i, j});
            }
            if (pond[i][j] == 'L' && sq.empty())  {
                sq.push({i, j});
                visited[i][j] = true;
            }
        }
    }

    int day = 0;

    while (true) {
        swan_bfs();
        
        if (!FOUND) {
            water_bfs();
            next_sq.swap(sq);
            next_wq.swap(wq);
        } else {
            cout << day << endl;
            return 0;
        }

        day++;
    }
}