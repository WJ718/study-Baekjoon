"""
Docstring for 투포인터.2470_두 용액

<입력>
N: 전체 용액 수 (2~100,000)
for N:
    용액의 특성값

<출력>
특성값이 0에 가장 가까운 용액을 만들어내는 두 특성값
(두 개 이상인 경우, 그 중 아무거나)

<접근>
투 포인터 사용, left+right가 0에 가장 가까운 것
==> 절대값 사용
"""

N = int(input())
solution = list(map(int, input().split()))
solution.sort()
best = float('inf')

left, right = 0, N-1

while left < right:
    s = solution[left] + solution[right]

    if abs(s) < best:
        best = abs(s)
        answer = [solution[left], solution[right]]

    if s < 0:
        left += 1
    else:
        right -= 1

print(*answer)
    
    


