"""
Docstring for 집합과 맵.1764_듣보잡

<입력>
1. N(듣 사람 수) M(보 사람 수)
2. for N : 이름
3. for M : 이름

*중복 X
<출력>
두 집단의 교집합에 해당하는 숫자와 이름을 사전순으로 출력한다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # MAX 500_000

listen = []
watch = set()

for _ in range(N):
    listen.append(input().strip())

for _ in range(M):
    watch.add(input().strip())

result = []

for name in listen:
    if name in watch: # O(1)
        result.append(name)

result.sort()

print(len(result))
for r in result:
    print(r)





