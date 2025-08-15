#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() 
{
    int N, M, S, T;

    cin >> N >> M;

    vector<vector<int>> adj(N + 1, vector<int>(N + 1, 0));

    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a][b] = c;
        adj[b][a] = c;
    }

    cin >> S >> T;

    vector<int> dist(N + 1, INT32_MAX);
    priority_queue<int> q;

    q.push(S);
    dist[S] = 0;

    while (!q.empty()) {

        int curr = q.top();
        q.pop();

        for (int i = 1; i <= N; i++) {
            if (adj[curr][i] != 0) {
                int w = adj[curr][i];
                int acc = w + dist[curr];
                if (acc < dist[i]) {
                    dist[i] = acc;
                    q.push(i);
                }
            }
        }
    }

    cout << dist[T] << endl;
}