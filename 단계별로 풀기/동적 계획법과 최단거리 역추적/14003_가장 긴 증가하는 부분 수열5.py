"""
14002번을 O(NlogN)로 푸는 문제

<접근>
1. 길이 확인
N번 반복은 같으나, O(N)의 DP 확인 대신 O(N log N)인 이분탐색 활용
@bisect 모듈: bisect_left(a, x) 시 리스트 a에 x가 들어갈 인덱스 반환


* lis[k] = k+1 길이의 수열의 가장 유리한 상태
* lis_idx[i] = lis가 저장된 arr의 인덱스 기록
* pos[i] = a[i]가 Lis의 몇 번째 위치에 들어갔는지 기록
* prev[i] = a[i] 이전에 들어있던 인덱스
"""
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())) # 0 base

lis = []
lis_idx = []
pos = [0] * (N)
prev = [-1] * N

# N
for i in range(N):
    x = arr[i]

    # log N
    k = bisect_left(lis, x) # k: x가 들어갈 인덱스

    # k가 lis에서 가장 마지막에 위치한 경우:
    if k == len(lis):
        lis.append(x) # lis 길이 PLUS
        lis_idx.append(i) # lis_idx

    # k가 중간에 끼는 경우
    else:
        # 해당 부분만 UPDATE
        lis[k] = x
        lis_idx[k] = i

    pos[i] = k

    # prev : 가장 마지막 lis 바로 전의 arr의 인덱스
    if k > 0:
        prev[i] = lis_idx[k-1]

max_len = len(lis)

path = []
idx = lis_idx[-1]

# 역방향으로 구함
while idx != -1:
    path.append(arr[idx])
    idx = prev[idx]

path.reverse()

print(max_len)
print(*path)









