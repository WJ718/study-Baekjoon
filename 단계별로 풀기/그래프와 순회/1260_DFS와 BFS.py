"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과 출력

<입력>
정점의 개수 N /  간선개수 M / 탐색 시작 정점 V
M번만큼 반복: 양방향 간선
"""
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

# DFS
visited_dfs = [False] * (N+1)
def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')

    for nxt in graph[v]:
        if not visited_dfs[nxt]:
            dfs(nxt)

# BFS
def bfs(v):
    visited_bfs = [False] * (N+1)
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for idx in graph[v]:
            if not visited_bfs[idx]:
                visited_bfs[idx] = True
                queue.append(idx) 

dfs(V)
print()
bfs(V)