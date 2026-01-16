"""
알고리즘 수업 - 깊이 우선 탐색 1

입력 : 
정점의 수 N, 간선의 수 M, 시작 정점 R
M개의 줄에 정보 u, v가 주어짐 (정점1, 정점2 // 가중치는 모두 1)

BFS ==> 
"""
import sys
from collections import deque
sys.setrecursionlimit(10**6) # 입력ㅈㅔ한

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph =[[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    # 그래프에 각 인덱스와 만나는 정점 저장
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort() # 오름차순 정렬

visited = [0] * (N+1)
order = 1
queue = deque([])

def bfs(node):
    global order
    visited[node] = order
    order += 1
    queue.append(node)

    while(queue):
        u = queue.popleft()

        for v in graph[u]:
            if visited[v] == 0:
                visited[v] = order
                order+=1
                queue.append(v)

bfs(R)

for i in range(1, N+1):
    print(visited[i])