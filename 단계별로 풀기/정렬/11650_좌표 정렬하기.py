"""
Docstring for 정렬.11650_좌표 정렬하기

<입력>
1.N개수
2. for N: 각 좌표

<출력>
오름차순 정렬
"""

N = int(input())

arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

for a in arr:
    print(*a)




