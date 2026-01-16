"""
백준 1697
2차원 배열 안에서 계산하는 문제
수빈은 세 가지 선택권이 있음
1. 현위치 + 1
2. 현위치 -1
3. 현위치 * 2

INPUT 
수빈의 위치 N, 동생의 위치 K

OUTPUT:
동생을 찾는 가장 빠른 시간은 몇 초인가 찾는 문제
"""
from collections import deque
MAX = 100_000

N, K = map(int,input().split())

arr = [0] * (MAX+1)
queue = deque([N])

while queue:
    x = queue.popleft()

    if x == K:
        print(arr[x])
        break

    for nx in (x-1, x+1, x*2):
        # *2 를 했을떄 100_000 이 나올 수 있으므로 0 <= nx <= MAX
        if 0<=nx<=MAX and arr[nx] == 0:
            arr[nx] = arr[x] + 1
            queue.append(nx)



