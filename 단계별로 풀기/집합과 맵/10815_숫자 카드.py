"""
Docstring for 집합과 맵.10815_숫자 카드

<입력>
* 중복 없음

1. N (상근이의 숫자 카드 개수 1~500_000)
2. for N : 카드의 숫자
3. M (전체 카드 개수 1~500_000)
3. for M : 카드의 숫자

<출력>
M에 대해, 상근이가 가지고 있다면 1, 없다면 0 출력

<접근>
있나 없나 확인 -> in 연산 사용 O(N)

"""
import sys
input = sys.stdin.readline

N = int(input())
user = set(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

# O(M + N)
for card in cards:
    if card in user:
        print(1, end = " ")
    else:
        print(0, end = " ")


