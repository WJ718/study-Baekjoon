"""
Docstring for 동적계획법2.7579_앱

N개의 앱, 필요한 바이트인 M
M만큼의 바이트를 얻기 위해 앱 비활성화의 최소 비용을 계산

N M
for N: app_memories[i] 
for N: remove_value[i]

시간복잡도 : O(M^2)
"""
N, M = map(int, input().split())
app = list(map(int, input().split()))
cost = list(map(int, input().split()))
MAX_COST = sum(cost)

# DP[x] = 비용을 x만큼 썼을 때, 최대의 메모리 값
DP = [0] * (MAX_COST + 1)

# 0 / 1 kanpsack
for i in range(N): 
    # DP update
    for c in range(MAX_COST, cost[i] - 1, -1):
        DP[c] = max(DP[c], DP[c- cost[i]] + app[i]) 


for i in range(MAX_COST+1):
    if DP[i] >= M:
        print(i)
        break


"""
헷갈렸던 DP 업데이트 로직

# DP[c- cost[i]] : i번째 앱을 사용하지 않은 상태의 DP값

<정방향으로 순회>
같은 i 반복문 안에서 이미 갱신된 DP[c - cost[i]]를 다시 참조하게 되어
i번째 앱을 여러 번 선택한 효과가 발생한다.

<역방향으로 순회>
DP[c - cost[i]]는 항상 이번 i 반복에서 아직 갱신되지 않은 값이므로
i 이전 앱들만 고려한 상태를 참조하게 된다. 따라서 각 앱은 최대 한 번만 선택된다.
"""








