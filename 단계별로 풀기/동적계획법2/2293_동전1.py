"""
Docstring for 동적계획법2.2293_동전1

N : 동전 가짓수
K : 목표 금액

동전을 얼마든지 써도 되니, K에 도달 할 수 있는 경우의 수 출력
* 순서가 바뀌는 것은 포함 x
"""

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

DP = [0] * (K+1)
DP[0] = 1

for coin in coins:
    for x in range(coin, K+1):
        DP[x] += DP[x-coin]

answer = DP[K]
print(answer)
