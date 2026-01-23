"""
Docstring for 정렬.2750_수 정렬하기

<입력>
1. N (1~1000) : 수의 개수
2. N개의 수

<출력>
오름차순으로 정렬한 결과 (한줄씩)


"""
N = int(input())
arr = []

for i in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

for a in arr:
    print(a)
