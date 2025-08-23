import sys
from collections import deque

sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def move_swan():
    next_q = deque()

    while swan_q:
        r, c = swan_q.popleft()

        if (r, c) == swan[1]:
            return True, None

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = 1
                if arr[nr][nc] == 'X':
                    next_q.append((nr, nc))
                else:
                    swan_q.append((nr, nc))

    return False, next_q


def melt_ice():
    next_water = deque()

    while water_q:
        r, c = water_q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 'X':
                arr[nr][nc] = '.'
                next_water.append((nr, nc))

    return next_water


swan = []
water_q = deque()

for r in range(R):
    for c in range(C):
        if arr[r][c] != 'X':
            water_q.append((r, c))
        if arr[r][c] == 'L':
            swan.append((r, c))

swan_q = deque([swan[0]])
visited = [[0] * C for _ in range(R)]
visited[swan[0][0]][swan[0][1]] = True

day = 0

while True:
    found, next_swan_q = move_swan()

    if found:
        break

    water_q = melt_ice()
    swan_q = next_swan_q
    day += 1

print(day)
