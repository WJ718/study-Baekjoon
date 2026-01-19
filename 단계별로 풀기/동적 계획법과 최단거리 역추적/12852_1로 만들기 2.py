"""
Docstring for 동적 계획법과 최단거리 역추적.12852_1로 만들기 2

<규칙>
1. X가 3의 배수면 3으로 나눈다
2. X가 2의 배수면 2로 나눈다
3. 1을 뺀다

<입력>
1 ~ 10^6 사이의 자연수 N

<출력>
첫째줄: 연산을 사용하는 횟수의 최솟값 출력
둘째줄: N을 1로 만드는 방법에 포함된 수 (거쳐가는 수)

<접근>
1. 최단거리 측정
    - DP 배열 설정: DP[X] = x를 1로 만드는 최소 연산 횟수
    
    // 점화식
    DP[1] = 0

    // 기본
    DP[i] = DP[i-1] + 1  # 이전 값에서 1을 더했을 때
    prev[i] = i - 1

    // 조건 추가
    if) i가 3의 배수이며 DP[i]가 DP[i // 3] + 1 보다 클 때:
        DP[i] = DP[i // 3] + 1
        prev[i] = i // 3

    if) i가 2의 배수이며 DP[i]가 DP[i // 2] + 1 보다 클 때:
        DP[i] = DP[i // 2] + 1
        prev[i] = i // 2



2. 경로 저장
- 경로 복원 배열: prev[X] -> X가 되기 전 수

"""
import sys
input = sys.stdin.readline

N = int(input())

DP = [float('inf')] * (N+1)
prev = [0] * (N + 1)

DP[1] = 0

for i in range(2, N+1):
    # 기본 조건 (-1)
    DP[i] = DP[i-1] + 1
    prev[i] = i-1

    # 추가 조건 (%3 & %2)
    if i % 3 == 0 and DP[i // 3] + 1 < DP[i]:
        DP[i] = DP[i//3] + 1
        prev[i] = i//3

    if i % 2 == 0 and DP[i // 2] + 1 < DP[i]:
        DP[i] = DP[i//2] + 1
        prev[i] = i // 2

path = []
cur = N

while cur != 0:
    path.append(cur)
    cur = prev[cur]

print(DP[N])
print(*path)






    


