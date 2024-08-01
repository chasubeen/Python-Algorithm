from collections import deque

## 입력
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

## 처리
# 새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N):
  # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
  while mydeque and mydeque[-1][0] > now[i]:
    mydeque.pop()
  # 덱의 마지막 위치에 현재 값 저장
  mydeque.append((now[i], i))
  # 덱의 1번째 위치에서부터 L의 범위를 벗어난 값을 덱에서 제거
  if mydeque[0][1] <= i - L:
    mydeque.popleft()
  # 덱의 1번째 데이터 출력
  print(mydeque[0][0], end = ' ')