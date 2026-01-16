"""


[입력]
보석 개수 N, 가방개수 K

N개 줄만큼:
Mi Vi

K 줄만큼:
Ci

[출력]
훔칠 수 있는 보석 가격 합의 최댓값
단, 가방에는 최대 한 개의 보석만 넣을 수 있다.
"""
import heapq

# 보석개수, 가방개수
N, K = map(int, input().split())

# jews = (무게, 가격)의 튜플 데이터
jews = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jews.sort() # 무게기준 정렬
bags.sort() # 용량기준 정렬

hq = []
result = 0
i = 0

# 가방에 담을 수 있는 모든 보석 힙에 추가
for bag in bags:
    # 조건: 보석 개수를 초과하지 않으며 무게가 가방을 초과하지 않아야 함
    while i < N and jews[i][0] <= bag:
        # 가장 가벼운 보석부터 힙의 왼쪽에 넣음
        heapq.heappush(hq, -jews[i][1]) # 이때, 음수로 넣으므로 가격이 가장 높은 보석이 가장 왼쪽에 위치함
        i += 1
    
    if hq:
        result += -heapq.heappop(hq) # 가격이 가장 높은 것을 골라야하므로, 음수로 바꿔서 pop

print(result)








