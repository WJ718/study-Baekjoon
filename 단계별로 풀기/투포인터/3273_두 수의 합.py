"""
Docstring for 투포인터.3273_두 수의 합

<입력>
n: 수열의 크기 
for n:
    수열의 요소
x: 조건이 될 자연수

<출력>
ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수

<접근>
투 포인터 -> list에서 포인터 옮겨가면서 양방향으로 탐색

"""
n = int(input())
arr = list(map(int, input().split()))
cnt = 0

x = int(input())

arr.sort()

# 포인터 지정
left, right = 0, n-1

while left < right:
    result = arr[left] + arr[right]

    if result == x:
        cnt += 1
        left += 1
        right -= 1

    elif result < x:
        left += 1

    else:
        right -= 1

print(cnt)



