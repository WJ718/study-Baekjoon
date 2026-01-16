import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 입력ㅈㅔ한

N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True) #  내림차순 정렬

visited = [0] * (N+1)
order = 1
queue = deque([])

def bfs(node):
    global order
    visited[node] = order
    order += 1
    queue.append(node)

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if visited[v] == 0:
                visited[v] = order
                order+=1
                queue.append(v)

bfs(R)

for i in range(1, N+1):
    print(visited[i])