"""
Docstring for 정렬.25305_커트라인

<입력>
N K (응시자, 상받는 사람)
for N : 점수

<출력>
상받는 커트라인
"""
N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

print(arr[K-1])


