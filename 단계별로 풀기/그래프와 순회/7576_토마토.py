from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())

# 토마토 배열 채우기
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()


dx = [-1,1,0,0]
dy = [0,0,-1,1]


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))

# BFS
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i] , y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            queue.append((nx,ny))

# 결과 계산
result = 0
for r in arr:
    for tomato in r:
        # 익지 않은 토마토가 있는 경우
        if tomato == 0:
            print(-1)
            exit(0)

        result = max(result, tomato)

print(result - 1) # 첫 루프가 1일이므로
