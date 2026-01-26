"""
Docstring for 약수, 배수와 소수2.2485_가로수

<입력>
1. 이미 심어진 가로수 수 (3 <= N <= 100_000)
2. for N : 가로수 위치

<출력>
모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소 수

<접근>
N크기의 배열에 차례대로 거리 정보 주어짐

1. 모든 간격 구하기 (Di)
2. D의 GCD 구하기

* 새로 심는 나무는 diff 배열에 저장된 거리를 공통 GCD로 나눈 값 - 1
* 정확히는 (d / g + 1) -  2 , d / g +  1 -> 나무 개수, -2 : 양 끝 나무 (이미 심어짐)
"""
from math import gcd

N = int(input())
trees = [int(input()) for _ in range(N)]

diff = []
for i in range(1, N):
    diff.append(trees[i] - trees[i-1])

# 공통된 GCD 구하기
g = diff[0]
for d in diff[1:]:
    g = gcd(g, d)

answer = 0
for d in diff:
    answer += d // g - 1 # ((d / g + 1) - 2) 

print(answer)