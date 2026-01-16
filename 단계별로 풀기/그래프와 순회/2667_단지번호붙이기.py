"""
백준 2667
정사각형 배열에 이어진 부분의 개수를 세기

입력: 배열의 가로 세로 크기 N & 1 or 0
출력: 각 단지의 크기를 오름차순으로 출력

DFS(재귀) 사용할 것

"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().strip())) for _ in range(N)]

# 좌 / 우 / 하 / 상
mx = [-1,1,0,0] 
my = [0,0,-1,1]

# 기본적으로 1인 곳만 DFS 사용
def DFS(x,y):
    # 방문한 곳 바꾸기
    area[x][y] = 0
    count = 1

    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        # 범위 안에 있으며 
        if 0 <= nx < N and 0 <= ny < N and area[nx][ny] == 1:
            count += DFS(nx,ny)

    return count

# 단지 수 저장할 리스트
result = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            result.append(DFS(i,j))

print(len(result))
for r in sorted(result):
    print(r)

    



