"""
Docstring for 집합과 맵.7758_회사에 있는 사람

<입력>
N(출입 기록 수)
for N: name (enter / leave)

<출력>
현재 회사에 있는 사람 이름 사전 역순으로 출력

<접근>
1. 딕셔너리에 enter = 1, leave = 0으로 저장.
2. 딕셔너리의 key값을 통해 1인 사람만 리스트로 추출
3. 리스트 역순 변환 출력
"""

N = int(input())
employees = {}

# O(N)
for i in range(N):
    name, state = map(str, input().split())

    if state == "enter":
        employees[name] = 1
    else:
        employees[name] = 0

result = []

# O(N)
for name in employees:
    if employees[name] == 1:
        result.append(name)

result.sort(reverse=True)

for r in result:
    print(r)



