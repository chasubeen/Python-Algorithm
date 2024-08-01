## 입력
N = int(input()) # 수열 내의 숫자 개수
A = list(map(int, input().split())) # 수열 리스트
ans = [0] * N # 결과 배열에는 숫자 저장
myStack = [] # 스택에는 인덱스 저장

## 처리
for i in range(N):
  # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 
  # 가리키는 수열보다 큰 경우
  while myStack and A[myStack[-1]] < A[i]:
    ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수를 현재 수열로 저장
  
  myStack.append(i)

# 반복문을 다 돌고도 스택이 안 빈 경우 
# -> 오큰수가 없는 경우
while myStack:
  ans[myStack.pop()] = -1

## 출력
for i in range(N):
  print(ans[i], end = ' ')