import sys

sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

s = input().strip()

cnt = {
    '0': 0,
    '1': 0
}
curr = s[0]
cnt[curr] += 1

for c in s:
    if c != curr:
        curr = c
        cnt[curr] += 1

print(min(cnt.values()))

