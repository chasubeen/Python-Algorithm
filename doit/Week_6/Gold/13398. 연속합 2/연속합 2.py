## 입력
N = int(input()) # 숫자 개수
A = list(map(int, input().split())) # 수열


## 처리
# 오른쪽으로 index를 포함한 최대 연속 합 구하기
L = [0] * N
L[0] = A[0]
result = L[0]

for i in range(1, N):
    L[i] = max(A[i], L[i-1] + A[i])
    result = max(result, L[i]) # 숫자를 제거하지 않았을 때 기본 최댓값으로 저장
    
# 왼쪽으로 index를 포함한 최대 연속 합 구하기
R = [0] * N
R[N-1] = A[N-1]

for i in range(N-2, -1, -1):
    R[i] = max(A[i], R[i+1] + A[i])

# L[i-1] + R[i-1] 2개의 구간 합 리스트를 더하면 i번째 값을 제거한 효과를 얻음
for i in range(1, N-1):
    temp = L[i-1] + R[i+1]
    result = max(result, temp)


## 출력
print(result)