n = int(input())
heights = []
stack = [] # 키, 같은 키 인원수 저장장
result = 0

# 두 사람 사이에 더 큰 키가 없으면 인사 가능. ==> 같은 키도 인사 가능
for _ in  range(n):
    current = int(input())
    count = 1

    # 현재 키가 top보다 크거나 같을 때
    while stack and current >= stack[-1][0]:
        # 인사 가능한 사람 pop
        height, cnt = stack.pop()
        result += cnt # 꺼낸 사람 수만큼 인사 가능 

        # 키가 같은 경우
        if current == height:
            count += cnt

    # 스택이 비어있지 않다 == 가장 최근의사람 & 남은 사람 중 가장 가까운 사람과 인사 가능
    if stack:
        result += 1

    stack.append((current, count))

print(result)
