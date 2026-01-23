"""
Docstring for 정렬.2587_대표값2

<입력>
다섯번째 줄까지: 자연수

<출력>
첫째줄 : 평균
둘째줄: 중앙값
"""
arr = []
total = 0

for i in range(5):
    num = int(input())
    arr.append(num)
    total += num

arr.sort()

print(total // 5)
print(arr[2])

