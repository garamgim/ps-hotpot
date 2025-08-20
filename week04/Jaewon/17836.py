import sys
from collections import deque

sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q = deque([(0, 0, 0)])  # (r, c, 시간)

    while q:
        r, c, w = q.popleft()
        if r == x and c == y:
            return w

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] != 1:
                visited[nr][nc] = 1
                q.append((nr, nc, w + 1))
    return -1

d1 = bfs(N-1, M-1)

d2 = 10000
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            d2 = bfs(r, c)
            if d2 != -1:
                d2 += abs(r - (N - 1)) + abs(c - (M - 1))

answer = min([x for x in [d1, d2] if x != -1], default=-1)

print(answer if 0 <= answer <= T else "Fail")
