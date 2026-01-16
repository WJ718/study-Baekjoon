"""
N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하라. 
단, A^B의 원소를 1000으로 나눈 나머지를 출력하라.

ans = A^B % 1000

# 접근법
N은 2~5의 숫자이고, 

"""

# NxN 행렬을 B제곱
N, B = map(int, input().split())

# 행렬 채우기
A = [list(map(int, input().split())) for _ in range(N)]

def matrixMul(A,B):
    N = len(A)
    # 반환 할 행렬
    result = [[0] * N for _ in range(N)] 

    # 곱하기 로직
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]

            result[i][j] %= 1000

    return result


def matrixPow(A, B):
    if  B == 1: 
        return [[a % 1000 for a in row] for row in A]

    half = matrixPow(A, B // 2) # 지수를 반으로 나눠가면서 재귀
    half_mul = matrixMul(half,half) 

    if B % 2 == 0:
        return half_mul
    else:
        return matrixMul(half_mul, A)
    
answer = matrixPow(A,B)

for row in answer:
    print(*row)


