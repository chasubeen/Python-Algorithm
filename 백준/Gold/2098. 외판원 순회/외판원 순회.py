import sys
input = sys.stdin.readline

## 입력
N = int(input()) # 도시 개수
# 비용 저장 리스트 
W = []
for i in range(N):
    W.append([])
    W[i] = list(map(int, input().split()))
# 최소 비용 저장 테이블
D = [[0 for j in range(1 << 16)] for i in range(16)]

# 완전 탐색 및 재귀 구현
def tsp(c,v):
    # 모든 도시를 방문했을 경우
    if v == (1<<N)-1:
        # 시작 도시로 돌아갈 수 있을 때
        if W[c][0] == 0:
            return float('inf')
        # 시작 도시로 돌아갈 수 없을 때
        else:
            return W[c][0]
    
    # 이미 계산한 적이 있을 때
    if D[c][v] != 0:
        return D[c][v]
        
    min_val = float('inf')
    for i in range(0, N):
        # 방문한 적은 없지만 갈 수 있는 도시일 때
        if (v & (1<<i)) == 0 and W[c][i] != 0:
            min_val = min(min_val, tsp(i, (v | (1 << i))) + W[c][i])
    D[c][v] = min_val
    return D[c][v]

## 출력
print(tsp(0,1))