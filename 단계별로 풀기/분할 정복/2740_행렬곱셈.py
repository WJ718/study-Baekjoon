"""
N*M크기의 행렬 A와 
M*K크기의 행렬 B가 주어졌을 때, 
두 행렬을 곱하는 프로그램을 작성하시오.

[입력] -  A의 크기 N 과 M, 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 주어짐
3 2
1 2
3 4
5 6
2 3
-1 -2 0
0 0 3

[출력] - 첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다.
-1 -2 6
-3 -6 12
-5 -10 18


[분할정복]
NxM , MxK 이므로 M을 기준으로 

N x (M/2) * (M/2) x K 반복하기

"""
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int,input().split())
B = [list(map(int, input().split())) for _ in range(M)]

# 재귀 알고리즘
def mul(A, B):
    N = len(A)
    M = len(A[0])
    K = len(B[0])

    if M == 1:
        return [[A[i][0] * B[0][j] for j in range(K)] for i in range (N)]

    # 분할
    mid = M // 2
    # A : 열의 일부를 자르기
    A1 = [row[:mid] for row in A]
    A2 = [row[mid:] for row in A]
    # B : 행의 일부를 자르기
    B1 = B[:mid]
    B2 = B[mid:]

    # 정복
    C1 = mul(A1, B1)
    C2 = mul(A2, B2)

    # 결합
    result = [[C1[i][j] + C2[i][j] for j in range(K)] for i in range(N)]
    return result

ans = mul(A,B)


for row in ans:
    print(*row)
