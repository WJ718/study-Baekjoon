"""
Docstring for 약수, 배수와 소수2.1929_소수 구하기

<입력>
M N (1 ~ 1_000_000)

<출력>
M이상 N이하의 모든 소수 출력

<접근>
소수 판별 -> 에라토스테네스의 체 사용
"""

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    # 소수의 배수를 제곱수까지 지워나가기
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False

for i in range(M, N+1):
    if is_prime[i]:
        print(i)
