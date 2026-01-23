"""
Docstring for 집합과 맵.14425_문자열 집합

<입력>
N(문자열 수 1~10_000) M(입력 개수)
for N : 집합 S
for M : 체크할 문자열

* 모두 소문자, 길이는 500이하, 중복 X

<출력>
M개의 문자열 중 몇 개가 S에 포함되었는가


"""
N, M = map(int, input().split())
S = []
checks = []

for i in range(N):
    S.append(str(input()))

for i in range(M):
    checks.append(str(input()))

cnt = 0

# O(M + N)
for check in checks:
    if check in S:
        cnt += 1

print(cnt)





