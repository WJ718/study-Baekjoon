"""
Docstring for 동적계획법2.11062_카드게임

DP[x][y] -> 현재 차례의 플레이어가 구간 [x ~ y] 에서 가질 수 있는 최대 점수
누적합 사용: 내 점수 == 해당 구간의 누적합 - 상대의 점수 

# 점화식
왼쪽 카드 고를 때 : 방금 생긴 점수 (cards[x]) + 모든 카드의 누적합 - 이번 단계의 상대의 점수(DP[x+1, y])
오른쪽 카드 고를 때 : 방금 생긴 점수 (cards[y] + 모든 카드의 누적합 - 이번 단계의 상대의 점수(DP[x, y-1]))

"""
T = int(input()) # TestCase

for _ in range (T):
    N = int(input())
    cards = list(map(int, input().split()))

    # 누적합 배열
    prefix = [0] * (N+1) 

    # 누적합
    for i in range(N):
        prefix[i+1] = prefix[i] + cards[i]

    # x구간부터 y구간까지의 누적합 구하는 함수
    def get_sum(x, y):
        return prefix[y+1] - prefix[x]
    
    DP = [[0] * N for _ in range(N)] # N x N 배열 생성, 각 인덱스는 0부터 시작

    # 구간 = 1
    for i in range(N):
        DP[i][i] = cards[i]

    # 구간 >= 2 따로 계산
    for length in range(2, N+1):
        # left
        for l in range(N - length + 1):
            # right
            r = l + length - 1

            # select: 각 양측 카드를 고를 때의 가치
            select_l = cards[l] + (get_sum(l + 1, r) - DP[l+1][r])
            select_r = cards[r] + (get_sum(l, r-1) - DP[l][r-1])

            DP[l][r] = max(select_l, select_r)

    print(DP[0][N-1])




    
    
    



 







