"""
1707-이분 그래프

1. DFS로 그래프 탐색하며 색 칠하기
2. 인접한 노드 다른 색으로 칠하기
3. 만약 인접한 노드가 자신과 같은 색으로 칠해졌다면 이분그래프가 X

[접근]
색 배열 생성 - (초기 모두 0, 진행하면서 1 or -1 저장)
모든 정점에 대해 아직 색이 없을 시 BFS 진행 
    * 다음 정점이 아직 색이 없으면 다른색으로 칠함
    * 이미 색이 있음 & 자신과 같은 색이면 break (이분G 아님)
"""
from collections import deque

# 테스트 케이스
K = int(input())

# 결과 저장 리스트
result = []

def BFS(start, graph, colors): 
    queue = deque()
    queue.append(start)
    
    colors[start] = 1 # 시작 컬러 => 1

    while queue:
        now = queue.popleft()

        for nxt in graph[now]:
            # 아직 색을 안입혔다면 현재와 다른 색
            if colors[nxt] == 0:
                colors[nxt] = -colors[now] # 반대 색 설정
                queue.append(nxt)
            # 색이 있는데 현재와 같은색이면 즉시 종료
            elif colors[nxt] == colors[now]:
                return False
    
    return True

for _ in range(K):
    V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
    graph = [[] for _ in range(V + 1)]
    colors = [0] * (V+1) # 색 저장 배열 1 / -1 

    for i in range(E):
        node1, node2 = map(int, input().split()) # 간선 정보
        # 그래프 생성
        graph[node1].append(node2)
        graph[node2].append(node1)

    checkBipartite = True

    for v in range (1, V+1):
        if colors[v] == 0:
            if not BFS(v, graph, colors):
                checkBipartite = False
                break
    
    print("YES" if checkBipartite else "NO")
    

    
    


