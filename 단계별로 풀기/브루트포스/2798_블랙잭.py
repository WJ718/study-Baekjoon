"""
Docstring for 브루트포스.2798_블랙잭

<입력>
카드 개수 N, 목표 수 M
카드 숫자 배열 arr[N]

<출력>
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합

<접근>
모든 경우의 수 확인 
1. 3중 for 문 -> O(N^3)
2. combination
"""
from itertools import combinations

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

MAX = M
answer = -1

for c in combinations(cards, 3):
    s = sum(c)
    if s <= MAX:
        answer = max(answer, s)

print(answer)

        






