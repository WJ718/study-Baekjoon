"""
백준 1012

입력
첫줄 : 테스트 케이스 개수 T

T번 반복:
    가로길이M / 세로길이N / 배추의 개수K 주어짐
        K번 반복: 
            배추의 위치 (X, y)주어짐


요점: 기본적으로 0으로 채워져 있는 필드를 생성하고, 배추의 위치가 나올 때마다 채워나감
 
그 후 DFS로 떨어져 있는 구역의 개수를 세기
             
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    global area
    area[y][x] = 0  # 방문 처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and area[ny][nx] == 1:
            DFS(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    area = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        area[y][x] = 1  # ⚠️ x=가로, y=세로

    result = 0
    for y in range(N):      # 세로 (행)
        for x in range(M):  # 가로 (열)
            if area[y][x] == 1:
                DFS(x, y)
                result += 1
    print(result)
