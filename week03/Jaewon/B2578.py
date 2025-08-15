import sys

sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
seq = [list(map(int, input().split())) for _ in range(5)]

def check_bingo():
    bingo = 0
    # 가로 빙고 확인
    for r in range(5):
        for c in range(5):
            if arr[r][c] != 0:
                break
        else:
            bingo += 1
    # 세로 빙고 확인
    for r in range(5):
        for c in range(5):
            if arr[c][r] != 0:
                break
        else:
            bingo += 1

    # 대각선 빙고 확인
    for r in range(5):
        if arr[r][r] != 0:
            break
    else:
        bingo += 1

    for r in range(5):
        if arr[r][4-r] != 0:
            break
    else:
        bingo += 1


    if bingo >= 3:
        return True

    return False


def play():
    for i in range(5):
        for j in range(5):
            for r in range(5):
                for c in range(5):
                    if arr[r][c] == seq[i][j]:
                        arr[r][c] = 0

            if check_bingo():
                return i * 5 + j + 1


print(play())
