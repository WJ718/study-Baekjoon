"""
Docstring for 브루트포스.2839_설탕 배달

<입력>
N (배달해야 하는 무게 3~5000)

<출력>
봉지의 최소개수, 정확하게 만들 수 없으면 -1 출력

<접근>
bag = 3kg, 5kg

1. 5KG 을 쓸 수 있을 때까지 사용
2. 더 이상 사용이 불가능 할 때 3KG을 사용

3-1. 모두 떨어지면 정답
3-2. N % 5를 3으로 나눌 수 없을 시 5kg봉지를 하나씩 줄여가면서 다시 계산

"""

N = int(input())
answer = -1

# 최대 5kg 가방 개수
five_kg = N // 5 

while five_kg >= 0:
    remain = N - (5 * five_kg)

    if remain % 3 == 0:
        answer = five_kg + (remain // 3)
        break

    else:
        five_kg -= 1

print(answer)

    

        






