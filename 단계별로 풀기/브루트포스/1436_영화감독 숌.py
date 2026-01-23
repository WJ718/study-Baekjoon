"""
Docstring for 브루트포스.1436_영화감독 숌

<입력>
N (1~10000)

<출력>
N번째 영화에 들어갈 수

<접근>
규칙: 666이 하나의 단위, 1666 -> 2666 -> 3666 ... 6666...

666부터 시작해서 순서대로 카운팅.
N번쨰의 수는 어떻게 판별할 것인가 -> cnt변수를 통해서 조건을 따짐. => while + break문
조건 판별은? i를 문자열로 바꾸고, "666"이 들어가는지 확인.


"""

N = int(input())

i = 666
part = "666"
cnt = 0

while True:
    str_i = str(i)

    if part in str_i:
        cnt += 1

    if cnt == N:
        break

    i+=1

print(i)
    





