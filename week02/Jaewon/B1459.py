import sys

# sys.stdin = open("../../input/input.txt", 'r')
# input = sys.stdin.readline

X, Y, W, S = map(int, input().split())
answer = 0

if 2 * W > S:
    X, Y = max(X, Y), min(X, Y)
    answer += Y * S

    if W > S:
        if (X - Y) % 2 == 0:
            answer += (X - Y) * S
        else:
            answer += (X - Y - 1) * S + W
        pass
    else:
        answer += (X - Y) * W

else:
    answer = (X + Y) * W

print(answer)