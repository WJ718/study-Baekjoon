"""
* 주사위는 1~6까지
* 보드판은 10 * 10 크기 --> 1차원 배열 사용

[인풋]
첫줄: 사다리의 수 N 뱀의수 M
둘째줄 ~ N개의 줄 사다리의 정보 x,y -- (x칸에 도착시 y번 칸으로 이동)
다음 M개의 줄 : 뱀의정보 (u,v) -- (u번칸에 도착하면, v칸으로 이동)

[아웃풋]
1번칸에서 출발해 100번칸에 도착하기 위해 주사위를 최소 몇 번 굴려야하는가
"""
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N: 사다리 / M: 뱀
N, M = map(int, input().split())
board = {}
visitied = [False] * 101
visitied[1] = True

# 사다리의 정보 입력
for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

# 뱀 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

queue = deque([(1,0)]) # (보드 위치 , 횟수)

# DFS
while queue:
    cur, cnt = queue.popleft()

    # 완료 조건
    if cur == 100:
        print(cnt)
        exit(0)

    # 주사위 굴리기
    for i in range(1, 7):
        next_cur = cur + i
        
        # 가지치기
        if next_cur > 100:
            continue

        if next_cur in board:
            next_cur = board[next_cur]
        
        # 처음 방문하는 칸 --> 표시 & 큐에 추가
        if not visitied[next_cur]:
            visitied[next_cur] = True
            queue.append((next_cur, cnt+1))



    

