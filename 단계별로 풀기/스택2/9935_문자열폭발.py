inputString = input() 
bomb = input()

# 임의의 스택 생성
stack = []

# 스택의 끝부터 확인할 길이 설정
bomb_len = len(bomb)

for char in inputString:
    stack.append(char)

    # 스택 끝부터 폭탄 길이만큼 확인
    # 스택의 끝부터 폭탄 길이만큼을 하나의 문자열로 보고, bomb 과 같을 시
    if ''.join(stack[-bomb_len:]) == bomb: 
        for _ in range(bomb_len): # 그만큼 pop
            stack.pop()

result = ''.join(stack)
print(result if result else "FRULA")
