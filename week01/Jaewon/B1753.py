import sys
import heapq

# sys.stdin = open("../../input/input.txt", 'r')
# input = sys.stdin.readline

INF = sys.maxsize

V, E = map(int, input().split())
adjl = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)
start = int(input())

for _ in range(E):
    s, e, w = map(int, input().split())
    adjl[s].append((e, w))


def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        d, node = heapq.heappop(q)

        if d > dist[node]:
            continue

        for next_node, weight in adjl[node]:
            next_dist = dist[node] + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))


dijkstra(start)

for i in range(1, V + 1):
    print(dist[i] if dist[i] != INF else "INF")



