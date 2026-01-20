"""
Docstring for 브루트포스.2231_분해합

<입력>
자연수 N (1 <= N <= 1,000,000)

<출력>
가작 작은 생성자 (없는 경우 0)

<접근>
*  X의 분해합은 X과 X을 이루는 각 자리수의 합 *
ex) 245 => 245 + 2 + 4 + 5 = 256

- X + (X의 자리 수 합) = N

# 분해합을 구하는 범위 -> 시간복잡도의 핵심

"""
import sys
input = sys.stdin.readline

N = int(input())
answer = 0

# 생성자 계산 함수
def decompositionSum(x):
    # 분해합을 리턴
    return x + sum(map(int, str(x)))

for i in range(N):
    if decompositionSum(i) == N:
        answer = i
        break

print(answer)










