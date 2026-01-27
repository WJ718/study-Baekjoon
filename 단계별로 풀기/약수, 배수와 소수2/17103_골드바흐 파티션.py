"""
Docstring for 약수, 배수와 소수2.17103_골드바흐 파티션

<입력>
T (테스트 케이스)
for T: N (짝수, 2<= N <= 1_000_000)

<출력>
골드바흐 파티션의 수 출력

<접근>
N을 두 소수의 합으로 나타낼 수 있는 조합의 개수 (순서 X)

1. 소수리스트 구하기 N log N
2. 소수 p와 q를 더했을 때 목표 입력 N
    => p가 최대 2/N이 될 때까지 브루트포스로 합 해보기
"""
T = int(input())
Ns = []

for i in range(T):
    Ns.append(int(input()))

MAX = max(Ns)
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# N log N
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j] = False
        
# N^2
for N in Ns:
    cnt = 0
    for i in range(2, (N//2) + 1):
        if is_prime[i] and is_prime[N-i]:
            cnt += 1
    
    print(cnt)






    






