"""
첫째 줄에 N, M이 주어진다.
N: 학생의 마지막 번호, M: 키를 비교한 횟수

<N번 반복>
A, B : A가 B보다 앞에 있다는 의미

<결과 출력>
학생을 앞에서부터 줄을 세운 결과 출력
"""
from collections import deque

N, M = map(int, input().split())

def topological_sort(n, edges): # n: 노드 개수 edges: A,  B 튜플로 이루어진 리스트

    graph = [[] for _ in range(N+1)]
    indegree = [0] * (n+1)

    for a, b in edges:
            # a가 b보다 먼저 실행되어야 함.
            graph[a].append(b)
            # 따라서 b의 진입 차수 1증가
            indegree[b] += 1

    # 진입 차수가 0인 노드 큐에 삽입
    queue = deque()

    # 진입차수 0 인것부터 큐에 적재
    for i in range(1, n+1):
          if indegree[i] == 0:
                queue.append(i)

    # 결과 저장 리스트
    result = []

    while queue:
        now = queue.popleft()
        result.append(now)

          
        for next in graph[now]:
                indegree[next] -= 1

                if indegree[next] == 0:
                      queue.append(next)
    
    return result

edges = []

for i in range(M):
      edges.append(list(map(int, input().split())))

answer = topological_sort(N, edges)

print(*answer)

