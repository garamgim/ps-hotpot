import sys
from collections import deque

# sys.stdin = open("../../input/input.txt", 'r')
# input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = deque()
    weights = list(map(int, input().split()))

    for idx, weight in enumerate(weights):
        q.append((idx, weight))

    answer = 0

    while q:
        idx, weight = q.popleft()

        for _, next_weight in q:
            if next_weight > weight:
                q.append((idx, weight))
                break
        else:
            answer += 1
            if idx == M:
                break

    print(answer)

