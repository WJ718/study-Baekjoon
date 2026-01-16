"""
[입력]
첫줄: 상자의 크기 M(가로칸),N(세로칸)   높이H
둘째줄 ~ N번쨰 줄: 토마토 정보 (0, -1, 1)

[출력]
토마토가 모두 익을 때까지 몇일이 걸리는지 출력
모든 토마토가 익어있는 상태라면 0, 
토마토가 모두 익지는 못하면 -1
"""
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

# tomato[1][2][3] -> 1층, 3줄(행), 4번째 칸(열)
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 1:
                queue.append((z,y,x))

while queue:
    z,y,x = queue.popleft()

    for i in range(6):
        nz, ny, nx = z + dz[i] , y + dy[i] , x + dx[i]

        if 0<=nz<H and 0<=ny<N and 0<=nx<M:
            # 안익은 토마토 탐색
            if tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                queue.append((nz,ny,nx))

result = 0

for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 0:
                print(-1)
                exit(0)

            result = max(result, tomato[z][y][x])
print(result - 1)
            




