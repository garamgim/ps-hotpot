import sys

# sys.stdin = open("../../input/input.txt", 'r')
# input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

l, r = 1, arr[-1]

answer = 0

while l <= r:

    m = (l + r) // 2

    idx = N - 1
    temp = 0
    while idx >= 0:
        temp += arr[idx] // m

        if arr[idx] < m:
            break

        idx -= 1

    if temp < M:
        r = m - 1
    elif temp >= M:
        answer = m
        l = m + 1

print(answer)