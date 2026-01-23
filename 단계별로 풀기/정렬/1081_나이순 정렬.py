"""
Docstring for 정렬.1081_나이순 정렬

<입력>
N(입력 데이터 개수)
for N (나이, 이름)

<출력>
1. 나이순 / 2. 가입순(입력 순서)

# 가입순서 -> sort 자체에서 입력순서 따짐
"""

N = int(input())

arr = []

for i in range(N):
    age, name = input().split()
    age = int(age)

    arr.append((age, name))

arr.sort(key = lambda x: (x[0]))

for age, name in arr:
    print(age, name)
