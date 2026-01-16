"""
홀수번째 수를 읽을 때 마다, 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.

1, 5, 4, 3, 2 이면, 
홀수번째 수는 1번째 수, 3번째 수, 5번째 수이고, 
1번째 수를 읽었을 때 중앙값은 1, 
3번째 수를 읽었을 때는 4, 
5번째 수를 읽었을 때는 3이다.

[입력]
테스트 케이스 개수 T

<반복>
수열의 크기 M
수열의 원소 차례대로 주어짐


[출력]
각 테스트 케이스에 대해:
    중앙값의 개수 출력
    홀수번째 수를 읽었을 때의 중앙값을 출력


<원리>
1. 새로운 수가 가장 크거나 max_heap이 비었다면 max_heap에 넣기
2. 그렇지 않으면 min_heap에 넣기
3. max_heap이 min_heap보다 2이상 크면, max힙의 요소를 min으로 이동
4. 반대일시, 반대    
"""
import heapq

testcase = int(input())

for _ in range(testcase):
    M = int(input())
    nums = []
    
    # ✅ 입력 처리 수정
    while len(nums) < M:
        nums += list(map(int, input().split()))

    left, right = [], []  # left: max_heap, right: min_heap
    medians = []

    for i in range(M):
        num = nums[i]

        if not left or num <= -left[0]:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        # 균형 유지
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

        # 홀수 번째 입력일 때 중앙값 기록
        if i % 2 == 0:
            medians.append(-left[0])

    # 출력
    print(len(medians))
    for i in range(0, len(medians), 10):
        print(*medians[i:i+10])
