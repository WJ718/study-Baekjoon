"""
[입력]
N - 수빈의 위치      K - 동생의 위치
[출력]
몇 번만에 동생의 위치로 가는가

[접근]
필드: 1차원 그래프
가중치: 시간(0초 / 1초)
비용: 최단거리

다익스트라로 거리를 비교

"""
from collections import deque
MAX = 1000000

N, M = map(int, input().split())

dist = [-1] * (MAX + 1)
dq = deque()
dq.append(N)
dist[N] = 0

# 데크 사용 이유 -> 순간이동은 appendleft / 걷기는 append 로 동시에 각각 계산
while dq:
    cur = dq.popleft()

    # 순간이동의 경우의 수
    ncur = cur * 2
    # 결과가 범위안에 있으며 dist계산을 안했으면 dist에 계산하고 dq에 삽입
    if 0 <= ncur <= 100000 and dist[ncur] == -1:
        dist[ncur] = dist[cur]
        dq.appendleft(ncur)

    for ncur in (cur-1, cur+1):
        if 0 <= ncur <= MAX and dist[ncur] == -1:
            dist[ncur] = dist[cur] + 1 # 걷기는 가중치 부여
            dq.append(ncur)

print(dist[M])

