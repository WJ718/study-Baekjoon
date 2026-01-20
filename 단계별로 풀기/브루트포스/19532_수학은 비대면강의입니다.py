"""
Docstring for 브루트포스.19532_수학은 비대면강의입니다

<입력>
a b c d e f

<출력>
ax + by = c
dx + ey = f
를 만족하는 x,y 값

* x와 y의 범위는 -999 ~~ 999이다.

<접근>
- 1999 x 1999 번의 완전탐색 O(N**2)
"""
import sys
sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c:
            if d*i + e*j == f:
                print(i, end = " ")
                print(j)
                break


