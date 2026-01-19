"""
Docstring for 동적 계획법과 최단거리 역추적.14002_가장 긴 증가하는 부분 수열4

<입>
첫쨰줄: 수열크기 N
둘째줄: 수열

<출>
길이 출력
가장 긴 증가하는 부분 수열 출력

<접근>
1. 수열 길이 저장
    DP[x] -> x번째 수로 끝나는 가장 긴 수열 길이

2. 길이 판별

// 점화식
DP[i] = max(DP[j] + 1) 이때, j는 i보다 작아야 함.

// 경로 복원
prev[i] = i번째 수 이전에 오는 수의 인덱스
"""

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split())) # 0 base

DP = [1] * (N)
prev = [-1] * (N) # 인덱스 저장

# O(N**2)
for i in range(N):
    for j in range(i):
        if array[j] < array[i] and DP[j] + 1 > DP[i]:
            DP[i] = DP[j] + 1
            prev[i] = j # save 'index'

max_len = max(DP) # 가장 긴 수열의 길이 찾기
idx = DP.index(max_len) # 그 때의 마지막 인덱스

path = []
while idx != -1:
    path.append(array[idx])
    idx = prev[idx]

path.reverse()

print(max_len)
print(*path)
        
