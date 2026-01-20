"""
Docstring for 동적 계획법과 최단거리 역추적.9252_LCS 2

<입력>
- str1
- str2

<출력>
- str1과 str2의 가장 긴 LCS 길이
- 그 경로 출력

<접근>
* 핵심 = 어떻게 두 문자열에 겹치는 수열을 찾을 것인가
    - DP[i][j] -> 앞 문자열의 i번째 문자와 뒷 문자열의 j 로 만들 수 있는 LCS 길이

    # 점화식
        if str1[i-1] == str[j-1] : DP[i][j] = DP[i-1][j-1] + 1
        else: DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    # 경로 출력
        각 문자열의 끝 인덱스부터 비교하면서 결과 배열에 저장
            * 판별 조건 1: str1[i] == str2[j]
            * 판별 조건 2: 아닐 시, DP[i-1][j] 이 더 큰가 DP[i][j-1]이 더 큰가?


"""
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

len1 = len(str1)
len2 = len(str2)

# DP -> [0~i][0~j]
DP = [[0] * (len2 + 1) for _ in range (len1 + 1)]


for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i-1] == str2[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1

        else: 
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

res = []

i, j = len1, len2

while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
        res.append(str1[i-1])
        i -= 1
        j -= 1

    # str1[i-1]과 str2[j-1]이 다른 경우
    else:
        # str1[i-1]을 버리는 게 더 긴 경우라면
        if DP[i-1][j] > DP[i][j-1]:            
            # str1[i-1] 를 버리고 다음 반복으로
            i -= 1
        else:
            j -= 1

res.reverse()

print(len(res))
print("".join(res))
    

