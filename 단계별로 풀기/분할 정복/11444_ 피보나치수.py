"""
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.

1. 재귀
--> 중복계산으로 인한 비효율성


2. 분할정복
"""

R = 1_000_000_007
n = int(input())

def matrixMul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % R,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % R],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % R,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % R]
    ]

def matrixPow(A, n):
    if n == 1:
        return A
    
    half = matrixPow(A, n //2)
    half_mul = matrixMul(half, half)

    if n % 2 == 0:
        return half_mul
    else:
        return matrixMul(half_mul, A)

if n == 0:
    print(0)
else:
    base = [[1,1] [1,0]]
    answer = matrixPow(base, n-1)
    print(answer[0][0])


