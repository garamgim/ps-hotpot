import sys
from collections import deque

sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

M, N = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

def bfs():
    visited[0][0] = 0
    q = deque()
    q.append((0, 0, 0))

    while q:
        r, c, weight = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                next_weight = weight + arr[nr][nc]
                if visited[nr][nc] == -1 or visited[nr][nc] > next_weight:
                    visited[nr][nc] = next_weight
                    if arr[nr][nc] == 1:
                        q.append((nr, nc, next_weight))
                    else:
                        q.appendleft((nr, nc, next_weight))

answer = 200
visited = [[-1] * M for _ in range(N)]

bfs()

print(visited[-1][-1])