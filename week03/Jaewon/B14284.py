import sys, heapq

INF = sys.maxsize
# sys.stdin = open("../../input/input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adjl[a].append((b, c))
    adjl[b].append((a, c))

s, t = map(int, input().split())

def djk(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, node = heapq.heappop(q)
        if d > dist[node]:
            continue
        for nxt, w in adjl[node]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(q, (nd, nxt))

    return dist

dist = djk(s)
print(dist[t])