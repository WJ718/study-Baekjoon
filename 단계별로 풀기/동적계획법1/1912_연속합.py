n = int(input())

numbers = list(map(int, input().split()))

# dp[i] 는 i번째에서 끝나는 연속합의 최댓값
dp = [0] * n 

dp[0] = numbers[0]
result = dp[0]

for i in range(1, n):
    # 이전까지의 결과에서 더할것인지, 새로 시작할 것인지
    dp[i] = max(numbers[i], dp[i-1] + numbers[i])
    # 최댓값 업데이트
    result = max(result, dp[i]) 

print(result)