"""
11657_타임머신

조건: 
* 1번부터 N번까지의 최소비용 구하기
* 음수사이클 발생하면 -1 출력하기

출력:
N-1개 줄에 걸쳐 각 줄에 N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다.
만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.
"""

N, M = map(int, input().split()) # N: 정점, M:간선
graph = [[] for _ in range(N+1)]
INF = float('inf')
dist = [INF] * (N+1) # 거리 배열

def BellmanFord(graph, N, dist):
    dist[1] = 0 # 정점 1 시작 -> 비용 0

    # 비용 계산
    for _ in range(N-1):
        for u in range(1, N+1):
            for v,w in graph[u]:
                if dist[u] != INF and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

    # 음수 사이클 계산
    for i in range(1, N+1):
        for v, w in graph[i]:
            # 거리가 또 줄어들면 음수사이클 발생
            if dist[i] != INF and dist[v] > dist[i] + w:
                return -1
    
    return True

for _ in range(M):
    u, v, w = map(int, input().split()) # 출발 - 도착 - 비용
    graph[u].append((v,w)) # 그래프 리스트는 튜플 저장 [출발지(도착지, 비용)]
    
result = BellmanFord(graph, N, dist)

if result == -1: # 음수 사이클로 판별났다면 -1 출력
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF: # 도달할 수 없다면 -1 출력
            print(-1)
        else:
            print(dist[i]) # 계산된 최소비용 출력




