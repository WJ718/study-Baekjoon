"""
입력: 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

츌력: 옮긴 횟수 K, 두번째 줄부터 수행 과정 A -> B

[접근방법]
초기 >> 3, 1, 3, 2 
그 다음 >> 2, 1, 2, 3
그 다음 

"""

N = int(input())

def move(start, to):
    print(start, to)

def hanoi(N, start, to, via): # 옮길 원반 개수, 출발지, 목적지, 경유지 
    if N == 1:
        move(start, to)
        return

    else:
        hanoi(N-1, start, via, to)
        move(start, to)
        hanoi(N-1, via, to, start)

print(2**N - 1)
hanoi(N, 1, 3, 2)




