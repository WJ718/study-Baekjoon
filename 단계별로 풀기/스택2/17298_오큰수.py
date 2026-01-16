"""
A(i) 의 오큰수는 A(i)보다 위에 있는 가장 최근에 삽입된 요소.
없으면 -1 로 출력
"""

n = int(input())

# 입력은 한줄로
nums = list(map(int, input().split()))
stack = [] # 인덱스가 저장될거임.
result = [-1] * n

for i in range(n):

    current = nums[i] # 비교 대상 - 실질적으로 1번 인덱스 부터 시작

    # 첫 반복에서는 처음에는 작동 X
    while stack and nums[stack[-1]] < current: # 스택이 비어있지 않고 & 비교대상이 기준 보다 클 때 # nums[stack[-1]] : 기준 수수
        index = stack.pop() # 오큰수를 못찾았던 숫자가 오큰수를 찾았으니 stack에서 pop되고, 그 인덱스는 결과를 찾은 것. --> while문을 통해 지금까지 지나친 인덱스도 다시 검토가능
        result[index] = current # 현재의 수가 오큰수이므로 결과로 저장 ex) result[0] = current #nums[1]

    stack.append(i) # 스택에 i 추가 - 0부터 시작 (번호를 저장)

for i in range(n):
    print(result[i] , end=' ')
















