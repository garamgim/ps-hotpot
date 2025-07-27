import sys
from collections import deque

# sys.stdin = open("../../input/input.txt", 'r')
# input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

max_v = 1

def bfs(r, c, water):
    q = deque([(r, c)])
    visited[r][c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] <= water:
                visited[nr][nc] = 1
                q.append((nr, nc))


for water in range(1, 99):

    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] <= water and not visited[r][c]:
                bfs(r, c, water)

    temp = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                bfs(r, c, 100)
                temp += 1

    max_v = max(max_v, temp)

print(max_v)
