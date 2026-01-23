"""
Docstring for 브루트포스.1018_체스판 다시 칠하기

<입력>
N M (8~50)
보드 상태

<출력>
다시 칠해야 하는 정사각형 개수의 최솟값

<접근>

보드를 8x8 으로 만들고, 그 안에서 몇 개의 칸을 조정해야 하는지 구한다.
보드의 시작이 W / B 일때 각각 구해야 하기 때문에, 보드를 다시 만들거나 수정하는것이 아니라

샘플을 각각 만들고, 값이 다른지 / 같은지를 판별한다

# 의사코드
for X in range(N-7): # N-1 에서 끝나기 때문에 -7
    for Y ..

        for i in range(8):
            for j in range(8):
                arr이 BW / WB와 다른지 같은지를 파별, 카운팅
"""

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

WB = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

BW = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

answer = float('inf')

# X와 Y 모두 최소 8칸
for X in range(N - 7):
    for Y in range(M - 7):
        cnt_WB = 0
        cnt_BW = 0

        for i in range(8):
            for j in range(8):
                if arr[X+i][Y+j] != WB[i][j]:
                    cnt_WB += 1
                
                if arr[X+i][Y+j] != BW[i][j]:
                    cnt_BW += 1

        answer = min(answer, cnt_WB, cnt_BW)

print(answer)
                





