import sys
input = sys.stdin.readline

## 입력
F = [0]*21 # 자리수 별로 만들 수 있는 순열의 수 저장
S = [0]*21 # 순열을 저장하는 리스트
visited = [False]*21 # 해당 숫자 사용 여부 리스트
N = int(input()) # 순열의 길이

## 처리
F[0] = 1
# 팩토리얼 초기화 → 각 자릿수에서 만들 수 있는 경우의 수
for i in range(1, N+1): 
    F[i] = F[i-1] * i

# 소문제 종류 및 순열 데이터 받기
inputList = list(map(int, input().split()))

# 1번 문항인 경우
if inputList[0] == 1:
    K = inputList[1] # 순열 순서
    for i in range(1,N+1):
        cnt = 1
        for j in range(1, N+1):
            if visited[j]:  # 이미 사용한 숫자는 사용할 수 없음
                continue
            if K <= cnt*F[N-i]: # 주어진 K에 따라 각 자리에 들어갈 수 있는 수 찾기
                K -= (cnt-1) * F[N-i]
                S[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, N+1):
        print(S[i], end=' ')

# 2번 문항인 경우
else:
    K = 1
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:
                cnt += 1    # 미사용 숫자 갯수 만큼 카운트
        K += cnt * F[N-i]   # 자릿수에 따라 순서 더하기
        visited[inputList[i]] = True
        
    ## 출력
    print(K)