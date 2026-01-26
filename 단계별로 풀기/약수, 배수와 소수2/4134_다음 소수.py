"""
Docstring for 약수, 배수와 소수2.4134_다음 소수

<입력>
T (테스트 케이스)
for T : N (정수) (0~4*10**9)

<출력>
각 T에 대해, N보다 크거나 같은 소수 중 가장 작은 것 줄 바꿔가며 출력

<접근>
소수 판별 : 에라토스테네스의 채

"""
T = int(input())
result = []
        
def isPrime(N):
    if N <= 1:
        return False
    
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    
    return True

def nextPrime(N):
    next_N = N

    while True:
        if isPrime(next_N):
            return next_N
        next_N += 1
    
for _ in range(T):
    number = int(input())
    answer = nextPrime(number)
    print(answer)


