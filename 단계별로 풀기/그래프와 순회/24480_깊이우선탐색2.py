import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N,M,R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse = True)

order = 1
visited = [0] * (N+1)

def dfs(node):
    global order
    visited[node] = order

    for idx in graph[node]:
        if visited[idx] == 0:
            order += 1
            dfs(idx)

dfs(R)

for i in range(1, N+1):
    print(visited[i])