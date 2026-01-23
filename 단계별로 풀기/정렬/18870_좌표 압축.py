"""
Docstring for 정렬.18870_좌표 압축

<입력>
1. N(좌표 개수)
2. for N : 좌표

<출력>
X'i = Xi를 좌표 압축한 결과

<접근>
X'i 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다
-> X'i 보다 작은 값의 개수를 인덱스에 저장

<문제가 있던 부분>
# 첫 코드
- 입력을 set으로 변환 후, 다시 list화 하여 정렬
- 해당 list에서 .index(X) 를 통해 순서를 알아내려 함
- .index() 연산이 O(N)이었기 때문에 시간초과 발생

* 해결
O(1)의 복잡도를 가지는 딕셔너리를 이용
*** 좌표압축 -> 딕셔너리에 enumerate와 함께 저장 ***
"""
N = int(input())

# 원본 입력
arr = list(map(int, input().split()))

# 중복 제거
new_arr = sorted(set(arr))

coord = {}
for i, v in enumerate(new_arr): # index, value
    coord[v] = i

for number in arr:
    print(coord[number], end = " ")











