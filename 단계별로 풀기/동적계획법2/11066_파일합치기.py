"""
Docstring for 동적계획법2.11066_파일합치기

*연속된 파일만 합칠 수 있음

<입력>
T : 테스트 케이스
K : 장수 (3~500)
    for K:
        파일의 크기 (list)

<출력>
모든 장을 합치는 데 필요한 최소비용

ex) 40 30 30 50일 때,
40 + 30 = 70
30 + 50 = 80
70 + 80 + 150 = 300

<접근>
k를 사용, 
구간을 i~k, k+1 ~j로 나눈다.

<점화식>
DP[i][j] = min(DP[i][k] + DP[k][j]) + sum(i~j) 
즉, i~j까지의 구간은 i~k, k+1~j까지의 구간이 계산 되어있어야함

"""

T = int(input())

for _ in range(T):
    # K : 파일 수
    K = int(input())
    arr = list(map(int, input().split()))

    # 누적합 -> SUM(I~J) 미리 구해놓기
    prefix = [0] * (K+1) # prefix는 arr보다 한 칸 더 길어야 함. (최종적인 길이도 구할 것이므로)
    for i in range(K):
        prefix[i+1] = prefix[i] + arr[i]

    # i~j 구간의 합을 구함
    def rangeSum(i, j):
        return prefix[j+1] - prefix[i]
    
    # DP[i][j] = i~j 구간을 하나로 합치는 최소 비용
    DP = [[0] * (K) for _ in range(K)]

    # length : 연속으로 합할 파일 길이
    for length in range(2, K+1):
        # i : 구간 시작점 , K-length+1 : i의 마지막 값
        for i in range(K - length + 1):
        
            # j: 해당 구간의 마지막 인덱스
            j = i + length - 1
            
            # 최소비용 찾기 위해 최댓값으로 초기화
            DP[i][j] = float('inf')

            for k in range(i, j):
                cost = DP[i][k] + DP[k+1][j] + rangeSum(i,j)
                # DP업데이트
                DP[i][j] = min(DP[i][j], cost)

    print(DP[0][K-1])


    




