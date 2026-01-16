heights = []

def calculate(heights):
    heights.append(0) # 마지막 막대까지 계산을 위해서 
    stack = [] # 인덱스 저장
    n = len(heights)
    result = 0
    max_size = 0

    for i in range(n):

        current = heights[i]

        # 스택이 비어있지 않으며 current가 stack의 top보다 작은 경우, 정리 필요
        while stack and current < heights[stack[-1]]:
            # 우선 인덱스 구함
            index = stack.pop()

            # 스택이 비어있다 = 큰 직사각형 넓이 구함. 너비는 i임
            # 스택이 비어있지 않다 = 부분 넓이 구함
            width = i if not stack else i - stack[-1] - 1
            result = heights[index] * width

            if(result > max_size):
                max_size = result

        stack.append(i)
    
    return max_size


n = int(input())

for i in range(n):
    heights.append(int(input()))

result = calculate(heights)

print(result)










