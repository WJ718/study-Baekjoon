"""
백준 11404
n(2~100) 개의 도시 => 정점
1~100,000 개의 버스 => 간선

모든 도시의 쌍(A, B)에 대한 최소값을 구하라
--> 모든 지점에서 다른 모든 지점까지의 최단 경로 구하기 

<입력>
n : 도시의 개수
m : 버스의 개수
(1~m): 간선정보 (A -> B, C) 

<출력>
(dist 2차원 배열 그대로 출력)
n개의 줄 출력 
i번째 줄에 출력되는 j번째 숫자 : i to j의 최소비용, 갈 수 없는 경우에는 0 출력
"""
INF = float('inf')

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [[INF] * (n+1) for _ in range(n+1)] # 2차원 테이블 형성

# 플로이드 구현
def Floyd(n, dist):
    for i in range(1, n+1):
        dist[i][i] = 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

for _ in range(1,m+1):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    
answer = Floyd(n, dist)

for i in range(1, n+1):
    for j in range(1, n+1):
        if answer[i][j] == INF:
            print(0, end = " ")
        else:
            print(answer[i][j], end = " ")
    print()




    





