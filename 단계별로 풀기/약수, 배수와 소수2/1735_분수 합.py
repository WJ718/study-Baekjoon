"""
Docstring for 약수, 배수와 소수2.1735_분수 합

<입력>
A B (분자 분모)
C D (분자 분모)

<출력>
A/B + C/D 결과를 '기약분수'

<접근>
1. B와 D의 최소공배수 구함
2. 더하기
"""

A, B = map(int, input().split())
C, D = map(int, input().split())

def gcd(B, D):
    while D != 0:
        r = B % D
        B = D
        D = r
    return B

same = (B*D) // gcd(B,D)
need_B = same // B
need_D = same // D

# 통분 필요
son = A * need_B + C * need_D
mother = same

g = gcd(son, mother)
son //= g
mother //= g

print(son, mother)


