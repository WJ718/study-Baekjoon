"""
NxM 행렬의 맵에서 (1,1) --> (N,M) 까지 이동하려고 할 때, 최단 경로로 이동하려 한다.

*시작하는 칸 포함해서 세기
*한 개의 벽은 부술 수 있다. <-- 핵심문제
*상하좌우로 이동할 수 있다
"""
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(N)]
queue = deque([(0,0,0)]) # x, y, broken
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, wall = queue.popleft()

    if x == N-1 and y == M-1:
        print(visited[x][y][wall])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            # 빈칸
            if map[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                queue.append((nx, ny, wall))
            
            # 벽을 부술 수 있는 경우
            elif map[nx][ny] == 1 and wall == 0:
                visited[nx][ny][1] = visited[x][y][wall] + 1
                queue.append((nx, ny, 1))


else:
    print(-1)


                


