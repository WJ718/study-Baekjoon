"""
알고리즘 수업 - 깊이 우선 탐색 1

입력 : 
정점의 수 N, 간선의 수 M, 시작 정점 R
M개의 줄에 정보 u, v가 주어짐 (정점1, 정점2 // 가중치는 모두 1)

DFS : deque 사용 or 재귀

"""
import sys
sys.setrecursionlimit(10**6) # 입력ㅈㅔ한

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph =[[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    # 그래프에 각 인덱스와 만나는 정점 저장
    graph[u].append(v)
    graph[v].append(u)

# 빠른 순회 위한 정렬
for i in range(1, N + 1):
    graph[i].sort()

visited = [0] * (N+1) 
# 전역변수 
order = 1 

def dfs(node):
    global order
    # visited => 방문 순서 기록 
    visited[node] = order 

    # 시작 노드와 연결된 정점부터 차례로 순회
    for idx in graph[node]:
        # 방문한 적이 없을 시
        if visited[idx] == 0:
            # 다음 호출에서 visited 에 기록
            order += 1
            dfs(idx)
dfs(R)

for i in range(1, N+1):
    print(visited[i])





