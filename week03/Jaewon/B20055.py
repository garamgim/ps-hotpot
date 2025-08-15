import sys
from collections import deque

# sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0] * N)

stage = 0

while True:
    stage += 1

    # 벨트 회전
    belt.appendleft(belt.pop())
    robots.appendleft(robots.pop())

    # 로봇 내리기
    robots[N-1] = 0

    # 로봇 이동시키기

    for i in range(N-2, -1, -1):
        # 다음칸에 로봇이 없고 내구도가 1 이상이면 로봇 이동
        if robots[i] == 1 and not robots[i + 1] and belt[i + 1] >= 1:
            robots[i] = 0
            robots[i + 1] = 1
            belt[i + 1] -= 1

    # 로봇 내리기
    robots[N - 1] = 0

    # 로봇 올리기
    if belt[0]:
        robots[0] = 1
        belt[0] -= 1

    # 내구도가 0인 칸 세기
    if belt.count(0) >= K:
        break

print(stage)