from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

def BFS(miro, N , M):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([(0,0)])

    while queue:
        # x : 행 / y : 열
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))   

    return (miro[N-1][M-1]) 

ans = BFS(miro,N,M)
print(ans)