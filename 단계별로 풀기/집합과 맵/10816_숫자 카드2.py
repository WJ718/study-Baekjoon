"""
Docstring for 집합과 맵.10816_숫자 카드2

<입력>
1. N(상근의 숫자카드 개수 1~~500_000)
2. for N: 숫자 입력
3. M(샘플 숫자카드 개수 1~500_000)
4. for M: 숫자 입력

<출력>
각 수가 적힌 숫자 카드를 몇 개나 가지고 있는지 공백으로 출력

<접근>
딕셔너리로 {card, 횟수} 저장

"""
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
sample = list(map(int, input().split()))

count = defaultdict(int)

# O(N)
for card in cards:
    count[card] += 1

# O(M)
for s in sample:
    print(count[s], end = " ")