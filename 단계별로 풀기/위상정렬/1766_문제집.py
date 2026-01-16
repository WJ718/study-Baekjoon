"""
백준 1766 

[입력]
N-(문제의 수) , M-정보의 개수
M번 반복:
    정수 순서쌍 A,B (A가 B보다 우선순위 높음)

[출력]
문제를 풀어야 하는 빈칸의 수

[접근방식]
최소 힙 사용 - 작은 번호부터 우선순위로 풀기
"""
import heapq

# 문제번호는 1~N, M = 정보 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 2차원 인접리스트 (모든 순서 작성 위해)
indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())

    graph[A].append(B)
    indegree[B] += 1

hq = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)

result = []

while hq:
    now = heapq.heappop(hq)
    result.append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(hq,nxt)

print(*result)
