import sys
sys.setrecursionlimit(10 ** 6) # 재귀 호출 범위 늘리기 
input = sys.stdin.readline

## 입력
N = int(input()) # 트리 노드 개수
visited = [False] * (N) # 방문 기록 저장
tree = [[] for _ in range(N)] # 그래프 데이터 저장 인접 리스트 
answer = 0 # 리프 노드 개수 저장
p = list(map(int, input().split())) # 입력 데이터 저장

## 처리
# 트리 그리기
for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i


# DFS 탐색 함수
def DFS(number):
    global answer
    visited[number] = True
    cNode = 0 # 자식 노드의 수
    for i in tree[number]:
        # 삭제 노드가 아닐 때도 탐색 중지
        if not visited[i] and i != deleteNode:  
            cNode += 1
            DFS(i)
    # 자식 노드가 0개이면 리프 노드이므로 정답 값 증가
    if cNode == 0:
        answer += 1  

## 출력
deleteNode = int(input()) # 삭제할 노드
if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)