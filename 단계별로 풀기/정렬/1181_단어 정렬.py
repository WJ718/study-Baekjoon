"""
Docstring for 정렬.1181_단어 정렬

<입력>
1. N (단어 개수)
2. for N (단어)

<출력>
1. 길이가 짧고
2. 사전순으로 정렬

<접근>
1. 중복된 단어는 하나만 남기고 제거

2. 일반적인 알파벳 순 정렬이 아닌, 
    1. 길이 / 2. 사전 두 가지 조건

따라서 람다식을 사용
* 람다식 문법
sort(key=lambda x: (조건))

"""
N = int(input())
str_arr = set()

for i in range(N):
    word = str(input())
    str_arr.add(word)

str_arr = list(str_arr)
str_arr.sort(key = lambda x: (len(x), x)) # 1. 길이     2. 알파벳

for s in str_arr:
    print(s)
