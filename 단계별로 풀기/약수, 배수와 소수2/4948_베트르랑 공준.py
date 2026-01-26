"""
Docstring for 약수, 배수와 소수2.4948_베트르랑 공준

<입력>
0이 나올때까지, 자연수 n

<출력>
각 케이스에 대해, n < X <= 2n에 해당하는 소수의 개수

<접근>
* 특정 범위 안의 소수의 개수 -> 에라토스테네스
"""

def getPrimeArray(n):
    end = n*2

    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, end+1):
        if is_prime[i]:
            for j in range(i*i, end+1, i):
                is_prime[j] = False
    
    return is_prime

while True:
    n = int(input())
    cnt = 0

    # 종료 조건
    if n == 0 :
        break

    prime_array = getPrimeArray(n)
    for i in range(n+1, n*2+1):
        if prime_array[i]:
            cnt += 1

    print(cnt)


    

