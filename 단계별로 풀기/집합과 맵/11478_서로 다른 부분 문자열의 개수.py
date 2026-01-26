"""
Docstring for 집합과 맵.11478_서로 다른 부분 문자열의 개수

<입력>
S (문자열 / 소문자 / 1_000 자 이하)

<출력>
서로 다른 부분 문자열의 개수

<접근>
슬라이싱

EX) abc / len = 3 , 마지막인덱스 - [2]

"""
S = str(input())
word_set = set()

# [0] ~ [N-1]
for left in range(len(S)):
    # [1] ~ [N]
    for right in range(left+1, len(S)+1):
        word_set.add(S[left:right])
    
print(len(word_set))
