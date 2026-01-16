n = int(input()) # test case

numbers = []
result = []

for i in range(n):
    numbers.append(int(input()))

dp = [0] * (max(numbers) + 1)
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, max(numbers) + 1):
    dp[i] = dp[i-2] + dp[i-3]

for num in numbers:
    result.append(dp[num])

for r in result:
    print(r, end = '\n')






