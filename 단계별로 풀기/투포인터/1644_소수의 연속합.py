"""
Docstring for 투포인터.1644_소수의 연속합

자연수가 주어졌을 때, 연속된 소수의 합으로 나타낼 수 있는가 확인

<입력>
목표 자연수
<출력>
소수의 합이 될 수 있는 경우의 수를 출력한다.

<접근>
'연속합' -> 소수로 이루어진 수열을 슬라이딩 윈도우로 확인

소수찾기 -> 에라토스테네스의 체(i가 2부터 N의 제곱근까지 나누어 떨어지는지 확인)
"""

N = int(input())

def getPrimeArr(N):
    arr = [i for i in range(N+1)] # 인덱스와 값을 동일하게 둔 배열 형성
    end = int(N**(1/2)) # N의 제곱근까지만 확인

    for i in range(2, end+1):
        # 이전 단계에서 지워진 수는 pass
        if arr[i] == 0:
            continue
        # 소수 거름망 => i*i ~> 더 작은 소수에서 지워짐 
        for j in range(i*i, N+1, i): 
            arr[j] = 0

    return [i for i in arr[2:] if arr[i]]

# 소수 리스트         
arr = getPrimeArr(N)

left, right = 0, 0
current = 0
cnt = 0

# 슬라이딩 윈도우 구현
while True:
    # 목표값 이상일 때
    if current >= N:
        # 정확하다면 경우의 수 추가
        if current == N:
            cnt += 1
        # 더 크다면 left 제거 & 칸 좁히기
        current -= arr[left]
        left += 1

    # 목표값보다 작을 때
    else:
        # 최대로 탐색했다면 종료
        if right == len(arr):
            break
    
        # 오른쪽 칸 넓히기
        current += arr[right]
        right += 1

print(cnt)



