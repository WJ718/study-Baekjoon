"""
Docstring for 정렬.2751_수 정렬하기2

N개의 수가 주어졌을떄, 오름차순 정리
"""

N = int(input())

arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

for i in range(N):
    print(arr[i])

