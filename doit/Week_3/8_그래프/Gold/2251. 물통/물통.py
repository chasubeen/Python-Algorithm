from collections import deque

## 그래프 정의
# 6가지 이동 경로를 0,1,2로 표현
# ex) 0 -> 1: A -> B
Sender = [0, 0, 1, 1, 2, 2] # 보내는 쪽
Receiver = [1, 2, 0, 2, 0, 1] # 받는 쪽

now = list(map(int, input().split())) # A,B,C 값 저장 리스트

# 방문 여부 저장 리스트(전체 용량이 200 이하)
visited = [[False for j in range(201)] for i in range(201)] 
# 정답 리스트
answer = [False] * 201

## 처리
def BFS():
    queue = deque()
    # 큐 자료구조에 출발 노드 더하기
    # A와 B가 0인 상태이므로 0, 0 노드에서 시작하기
    queue.append((0, 0))
    visited[0][0] = True
    
    # 현재 C 값 check
    answer[now[2]] = True
    
    ## 큐가 빌 때까지
    while queue:
        now_Node = queue.popleft() # 큐에서 노드 데이터 가져오기\
        # 데이터를 이용해 값 초기화
        A = now_Node[0] 
        B = now_Node[1]
        C = now[2] - A - B  # C는 전체 물의 양에서 A와 B를 뺀 것
        
        # A → B, A → C, B → A, B → C, C → A, C → B
        for k in range(6):  
            next = [A, B, C]
            next[Receiver[k]] += next[Sender[k]]
            next[Sender[k]] = 0

            # 물이 넘칠 때
            # 초과하는 만큼 다시 이전 물통에 넣어주기
            if next[Receiver[k]] > now[Receiver[k]]:
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]]
                next[Receiver[k]] = now[Receiver[k]]  # 대상 물통 최대로 채우기
            if not visited[next[0]][next[1]]:  # A와 B의 물의 양으로 방문 리스트 체크
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0:  # A의 물의 양이 0일때 C의 물의 무게를 정답 변수에 저장
                    answer[next[2]] = True

BFS()

## 출력
for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')