# 빠른 입출력 처리
import sys
input = sys.stdin.readline

## 입력
n,m = map(int, input().split()) # 수열의 개수, 나누는 수
A = list(map(int, input().split())) # 원본 수열을 저장하는 리스트

## 처리
# 공간 초기화
S = [0] * n # 합 배열 선언 및 초기화
C = [0] * m # 같은 나머지의 인덱스를 카운트하는 리스트
            # 일단 각각의 수가 다 고유하다고 가정(?)
            
S[0] = A[0] # prefix 지정
answer = 0

# 합 배열 만들기
for i in range(1,n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m # 나머지 연산 수행
    # Case 1) 나머지 자체가 0
    if remainder == 0:
        answer += 1
    
    C[remainder] += 1 # 나머지가 같은 인덱스의 개수값 1 증가

# Case 2) 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수
for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2) # nC2 = (n * (n-1)) // 2

## 출력
print(answer)