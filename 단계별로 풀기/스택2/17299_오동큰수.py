"""
Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미

A = [1, 1, 2, 3, 4, 2, 1]
F1 = 3
F2 = 2
F3 = 1
F4 = 1

Ai보다 오른쪽에 있으면서, 해당 인덱스 (nums[j]) 가 해당되는 F_stack[nums[j]] 이 F_stack[nums[i]]보다 큰 경우 그 Fi의 i값을 결과스택에 넣음. 기본 -1

"""

n = int(input())
nums = list(map(int, input().split())) # 사용자가 입력하는 수열
stack = []
result = [-1] * n # 결과 스택은 -1로 채워놓음
F = {}   # 각 숫자의 횟수 저장

for num in nums:
    if num in F:
        F[num] += 1
    else:
        F[num] = 0

# print(F) // 확인용 로그 --> 3 1 2 1 에 대해 {3: 0, 1: 1, 2: 0} 으로 저장

for i in range(n):
    current = nums[i]

    # 횟수로 비교
    while stack and F[nums[stack[-1]]] < F[current]: # 이후에 나온 수 중 등장횟수가 더 많은 수가 있다면
        index = stack.pop() # stack에서 기준 수의 인덱스를 pop, 
        result[index] = current # 결과 스택에 해당 수를 채우고 다음 반복으로 

    stack.append(i)

for i in range(n):
    print(result[i], end = ' ')


