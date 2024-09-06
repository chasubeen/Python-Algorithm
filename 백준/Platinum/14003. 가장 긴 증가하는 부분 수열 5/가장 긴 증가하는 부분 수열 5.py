import sys
input = sys.stdin.readline

## 입력
n = int(input())  # 수열 개수

A = list(map(int, input().split()))  # 수열 데이터 저장 리스트
A.insert(0,0)

index = 0
maxLength = 1 # 가장 긴 증가하는 부분 수열 길이 저장

B = [0] * 1000001 # 현재 가장 유리한 증가 수열 저장 리스트
B[maxLength] = A[1]  # B[1] = A[1]으로 초기화

D = [0] * 1000001  # 최장 증가 수열의 길이 저장 리스트
D[1] = 1 
ans = [0] * 1000001 # 정답 수열 저장 리스트


## 처리
# binary search 구현
# 현재 수열이 들어갈 수 있는 위치를 빠르게 찾기 위한 함수
def binarySearch(l, r, now):
    while l < r:
        mid = (l + r) // 2  # 중앙값
        if B[mid] < now:
            l = mid + 1 
        else:
            r = mid 
    return l 

for i in range(2, n+1):
    # 가장 마지막 수열보다 현재 수열이 크면 
    if B[maxLength] < A[i]:  
        maxLength += 1 
        B[maxLength] = A[i]
        D[i] = maxLength 
    else:  
        index = binarySearch(1, maxLength, A[i])
        B[index] = A[i]
        D[i] = index 
        
print(maxLength) # 가장 긴 증가하는 수열 길이 출력

index = maxLength 
# x = B[maxLength] + 1 

# 뒤에서부터 탐색하면서 정답 수열 저장 
for i in range(n, 0, -1):
    # 최초 maxLength와 같은 값을 지닌 D 리스트 index를 찾아 해당 수열 저장
    if D[i] == index: 
        ans[index] = A[i]
        index -= 1 # 인덱스 감소

## 출력
for i in range(1, maxLength + 1):
    print(ans[i], end=' ')