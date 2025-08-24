#include <iostream>
#include <vector>
#include <queue>

using namespace std;

char map[300][300];
bool visited[300][300];
int R, C, x, y, x2, y2;
int dr[4] = {-1, 1 ,0, 0};
int dc[4] = {0, 0, -1, 1};
queue<pair<int, int>> wall, q;

bool jump() {
    while (!q.empty()) {
        pair<int, int> coord = q.front();
        q.pop();

        for (int d = 0; d < 4; d++) {
            int nr = coord.first + dr[d];
            int nc = coord.second + dc[d];

            if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                if (map[nr][nc] == '0' && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.push({nr, nc});
                } else if (map[nr][nc] == '1' && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    wall.push({nr, nc});
                } else if (map[nr][nc] == '#') {
                    return true;
                }
            }
        }
    }
    
    return false;
}

void destroy() {
    while (!wall.empty()) {
        pair<int, int> coord = wall.front();
        wall.pop();
        q.push(coord);
        map[coord.first][coord.second] = '0';
    }
}

int main() 
{
    cin >> R >> C >> x >> y >> x2 >> y2;
    x--;
    y--;
    x2--;
    y2--;

    q.push({x, y});
    visited[x][y] = true;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> map[i][j];
        }
    }

    int jump_count = 0;

    while (true) {
        jump_count++;

        if (jump()) {
            cout << jump_count << endl;
            return 0;
        } else {
            destroy();
        }
    }
}