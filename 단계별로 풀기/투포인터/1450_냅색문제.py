"""
Docstring for 투포인터.1450_냅색문제

N개의 물건을 C만큼의 무게를 넣을 때, 가방에 넣을 수 있는 방법의 수 구하기

입력: N, C
     array # N개만큼, 물건의 무게를 의미
        
출력: 자연수 Result

<접근>
'가방에 담을 수 있는 모든 경우의 수' -> DP배열 (DP[w] = 무게 W까지 담았을 때의 가치)
"""


""" 초기 풀이 -> C가 너무 큰 수이기 때문에 메모리초과 발생 """
# N,C = map(int, input().split())
# weight = list(map(int, input().split()))

# # DP[i] = i번 물건까지 확인한 경우 중 무게 i를 만들 수 있는 경우의 수
# DP = [0] * (C+1)
# DP[0] = 1 # 아무 물건도 안 넣을 때의 경우 = 1

# # 무게가 w인 물건 탐색에 추가
# for w in weight:
#     for current in range(C, w-1, -1): # C부터 시작해서 w까지 하나씩 줄여가며 탐색
#         # 경우의 수 추가 -> w를 계산하기 전의 방법 각각에 대해, w를 추가할 수 있음
#         DP[current] += DP[current - w]

# print(sum(DP))


""" 두번째 풀이 -> Meet in the middle -> N을 반으로 나누어 부분탐색해서 더하기 """
from itertools import combinations

N,C = map(int, input().split())
weight = list(map(int, input().split()))

# 중간점 생성
mid = N // 2

left_w = weight[:mid]
right_w = weight[mid:]

subsum_left = []
subsum_right = []

for i in range(len(left_w) + 1):
    comb_left = combinations(left_w, i) # left_w 리스트 안에서 i개로 만들 수 있는 조합 생성 ex)(1,2)

    for comb in comb_left:
        subsum_left.append(sum(comb)) # 찾은 조합의 무게 합 저장

for i in range(len(right_w) + 1):
    comb_right = combinations(right_w, i)

    for comb in comb_right:
        subsum_right.append(sum(comb))


subsum_left.sort()
ans = 0

# subsum_left + subsum_right 이분탐색으로 진행

# 오른쪽 부분집합의 수를 고정시킴
for element_r in subsum_right:

    if element_r > C:
        continue
    
    # 첫 인덱스부터 시작, left 부분집합의 마지막 요소까지 확인
    start = 0
    end = len(subsum_left) - 1

    while start <= end:
        # 시작점 정하기
        mid = (start + end) // 2
        
        # 값이 초과할 시 시작점 DOWN
        if subsum_left[mid] + element_r > C:
            end = mid - 1
        
        # 값이 작거나 같을 때 시작점 UP
        else:
            start = mid + 1

    # end : 조건 만족하는 subsum_left의 마지막 인덱스 (0부터 시작했으므로 1 더해주기)
    ans += end + 1

    # 결과적으로 right_w의 조합을 고정적으로 선택하며 left_w의 요소만 이분탐색으로 체크
print(ans)
