import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

N, M = map(int, input().split())
x1, y1, x2, y2 = (v - 1 for v in map(int, input().split()))
arr = [list(input().strip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

q = deque()
q.append((x1, y1))

nxt_q = deque()
visited[x1][y1] = 1

def bfs():

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:

                if arr[nr][nc] == '1':
                    visited[nr][nc] = 1
                    nxt_q.append((nr, nc))
                elif arr[nr][nc] == '0':
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                elif arr[nr][nc] == '#':
                    return True

    return False


answer = 0
while True:
    answer += 1

    result = bfs()
    if result:
        break

    for r, c in nxt_q:
        arr[r][c] = '0'

    q = deque(nxt_q)
    nxt_q.clear()

print(answer)