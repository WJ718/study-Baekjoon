"""
Docstring for 집합과 맵.1269_대칭 차집합

<입력>
집합 크기 A, B (200_000 이하)
A_list 
B_list

<출력>
(A-B) + (B-A)
차집합 -> set 간 빼기
"""
A, B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

answer = len((A_set - B_set)) + len((B_set - A_set))
print(answer)







