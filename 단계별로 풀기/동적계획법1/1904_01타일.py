"""
타일은 00 / 1 로만 이루어져있음.

dp[1] = 1가지의 경우
dp[2] = 2가지의 경우
dp[3] = 1+2의 경우
...
"""

n = int(input())

dp = [0] * (n + 2)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])
    

