"""
입력
1. 컴퓨터의 수
2. 직접 연결된 컴퓨터 쌍의 수
3. 그 수만큼의 무방향으로 이어진 정점


출력
1번 컴퓨터와 연결된 컴퓨터의 개수


접근방법
bfs 사용
"""
from collections import deque

N = int(input()) # 컴퓨터 개수
M = int(input()) # 서로 연결된 컴퓨터 개수
graph = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N+1)
queue = deque([])

# 시작 노드는 1번
def bfs(node = 1):
    visited[node] = True
    queue.append(node)

    while queue:
        u = queue.popleft()

        for each in graph[u]:
            # 방문 리스트에 없을 때만 추가
            if not visited[each]:
                visited[each] = True
                queue.append(each)

bfs(1)

answer = (sum(visited) - 1)
print(answer)




