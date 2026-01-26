"""
Docstring for 약수, 배수와 소수2.1934_최소공배수

<입력>
T(테스트케이스)
for T: A, B

<출력>
A와 B의 최소공배수

<접근>
최소공배수 = A X B // 최대공약수

"""

# 최대공약수
def getGcd(a, b):
    while b != 0:
        r = a % b
        a = b 
        b = r

    return a


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    gcd = getGcd(A, B)
    print(A*B // gcd)


    



