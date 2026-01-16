"""
Docstring for 투포인터.1806_부분합

<입력>
N(수열 길이) S(부분합 조건) 
for N :
    수열 요소

<출력>
합이 S 이상이 되는 것 중 가장 짧은 수열의 길이

<접근>
수열 => 정렬 불가

두 수가 아닌 여러개의 연속된 수를 구해야 함
=> 슬라이딩 윈도우 (left는 0, right 또한 0부터 시작해서 점진적으로 증가)

* current_sum = left + right
  current_sum < S --> right++ & updating current_sum 
  current_sum > S --> reserve answer & current_sum -= [arr[left]] & left += 1  
"""
# S를 넘기는 가장 짧은 수열의 길이 구하기
N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0 
current_sum = 0
answer = float('inf')

# 슬라이딩 윈도우
for right in range(N):
    current_sum += arr[right]

    # 조건보다 큰 경우
    while current_sum >= S:
        answer = min(answer, right - left + 1)
        # 부분합 요소를 줄여도 조건에 부합하는지 확인
        current_sum -= arr[left]
        left += 1


if answer == float('inf'):
    print(0)
else:
    print(answer)










    





