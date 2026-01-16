"""
Docstring for 최단경로.1956_운동

<문제>
사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾기
불가능한 경우 -1 출력

<입력>
V E (정점개수, 간선개수)
for E:
    a, b, c (지점1, 지점2, 비용) 

<출력>
사이클이 이루어질 때의 최소비용

<접근>
플로이드로 모든 지점간의 비용을 구하고, 다시 시작점으로 돌아올 수 있는 경우를 탐색
 - i에서 시작해서 i로 돌아오는 경우 사이클이 생김
 - 따라서 i -> j -> i로 돌아오는 경우 탐색 
"""
V, E = map(int, input().split())
INF = float('inf')
dist = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

def floyd(V, dist):
    for i in range(V+1):
            dist[i][i] = 0

    for k in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

floyd_dist = floyd(V, dist)

ans = INF

# i -> j -> i로 돌아오는지 탐색
for i in range(1, V+1):
    for j in range(1, V+1):
        # i와 j가 같은 경우 (자신이 자신으로 가는 것이므로 제외)
        if i != j:
            # (i to j) + (j to i)
            ans = min(ans, dist[i][j] + dist[j][i])

print(-1 if ans == INF else ans)

        



