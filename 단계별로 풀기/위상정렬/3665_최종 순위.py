from collections import deque

n = int(input()) # 테스트 케이스

for _ in range(n):
    team = int(input()) # 팀의 수
    last = list(map(int, input().split())) # 작년 등수

    # 현재까지의 정보로 그래프 원본 생성
    graph = [[False] * (team + 1) for _ in range(team + 1)] # 2차원 인접 행렬
    indegree = [0] * (team+1)

    for i in range(team):
        for j in range(i+1, team):
            a = last[i]
            b = last[j]
            graph[a][b] = True
            indegree[b] += 1
            
    # 순위 변경 과정
    change = int(input()) 
    for _ in range(change):
        a, b = map(int, input().split())

        # 진입차수 조정
        if graph[a][b]:
            # 사이클 탐색 위해 그래프 조정
            graph[a][b] = False
            graph[b][a] = True
            # 진입차수 반대로
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    # 판별 위한 큐 생성
    queue = deque()
    # 진입차수가 0인 노드를 먼저 큐에 삽입 -> 큐에 둘 이상 삽입될 시 순위 확정X
    for i in range(1, team+1):
        if indegree[i] == 0:
            queue.append(i)
        
    # 결과 저장 리스트
    result = []
    # 모호성
    ambiguous = False

    for _ in range(team):
        # 진입차수가 0인 노드 없을 시 - 선행조건 실패(사이클 발생)
        if not queue:
            print("IMPOSSIBLE")
            break

        if len(queue) > 1:
            ambiguous = True
    
        # 진입차수가 0인것부터 결과리스트에 넣음
        now = queue.popleft()
        result.append(now)

        # 넣은 노드와 연결된 노드들을 반복해가며
        for i in range(1, team + 1):
            if graph[now][i]:
                # 진입차수를 하나씩 뺀다
                indegree[i] -= 1
                # 진입차수가 0인 것을 다시 큐에 넣어 순위를 측정할 수 있는지 확인한다.
                if indegree[i] == 0:
                    queue.append(i)    
    else:
        if ambiguous:
            print("?")
        else:
            print(*result)

            

        
    


          




"""
팀의 수 (team)
작년에 i등을 한 팀의 번호 (edge)
등수가 바뀐 쌍의 수 (m)
상대적 등수가 바뀐 두 팀 (re_edge)

"""
            





