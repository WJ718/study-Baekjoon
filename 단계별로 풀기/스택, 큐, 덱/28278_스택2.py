# 명령어 수
n = int(input())

stack = []
result = []

for i in range(n):
    num = list(map(int, input().split()))
    
    if num[0] == 1:
        integer = num[1]
        stack.append(integer)

    elif num[0] == 2:
        if stack:
            integer = stack.pop()
            result.append(integer)
        else:
            result.append(-1)

    elif num[0] == 3:
        stack_len = len(stack)
        result.append(stack_len)
    
    elif num[0] == 4:
        if stack:
            result.append(0)
        else:
            result.append(1)
        
    elif num[0] == 5:
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)


for i in result:
    print(i)
