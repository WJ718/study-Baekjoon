from collections import deque

T = int(input())

# 나이트가 움직일 수 있는 칸
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

for _ in range(T):
    L = int(input())
    graph = [[0]*L for _ in range(L)]

    # 나이트의 현재 위치
    x1,y1 = map(int, input().split())
    # 목표 위치
    x2, y2 = map(int, input().split())
    graph[x2][y2] == 1

    if (x1, y1) == (x2, y2):
        print(0)
        continue

    queue = deque([(x1,y1)])
    graph[x1][y1] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<L and 0<=ny<L and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))


                if (nx,ny) == (x2,y2):
                    print(graph[nx][ny] - 1)
                    queue.clear()
                    break
                