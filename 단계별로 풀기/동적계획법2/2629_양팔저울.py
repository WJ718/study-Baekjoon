"""
Docstring for 동적계획법2.2629_양팔저울

<입력>
N (추의 개수 <= 30)
for N : 추의 무게 (<= 500)
checkN (확인할 구슬 개수)
for check N: 구슬의 무게(<= 40,000)
"""
# 추
N = int(input())
weight = list(map(int, input().split()))

# 구슬
M = int(input())
beads = list(map(int, input().split()))

limit = sum(weight)
DP = [False] * (limit+1)
DP[0] = True

for w in weight:
    new_DP = DP[:]

    for d in range(limit + 1):
        if DP[d]:
            if d + w <= limit:
                new_DP[d+w] = True
                new_DP[abs(d-w)] = True

    DP = new_DP # update DP array

for bead in beads:
    if bead <= limit and DP[bead]:
        print("Y", end=" ")
    else:
        print("N", end=" ")


