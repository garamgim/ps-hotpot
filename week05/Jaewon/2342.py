import sys
# sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

# 이동 비용 함수
def move_cost(start, to):
    if start == to:
        return 1
    if start == 0:
        return 2
    if abs(start - to) == 2:
        return 4
    return 3


sequence = list(map(int, input().split()))
sequence.pop()
n = len(sequence)

INF = 9
# dp[idx][l][r] = idx번째 지시까지 수행했을 때 최소 힘
dp = [[[INF] * 5 for _ in range(5)] for _ in range(n+1)]
dp[0][0][0] = 0

for idx in range(n):
    nxt = sequence[idx]

    for l in range(5):
        for r in range(5):

            if dp[idx][l][r] == INF:
                continue

            dp[idx+1][nxt][r] = min(dp[idx+1][nxt][r],
                                    dp[idx][l][r] + move_cost(l, nxt))
            dp[idx+1][l][nxt] = min(dp[idx+1][l][nxt],
                                    dp[idx][l][r] + move_cost(r, nxt))


answer = INF
for l in range(5):
    for r in range(5):
        answer = min(answer, dp[n][l][r])

print(answer)
