from collections import deque # queue를 위한 라이브러리

## 입력
N = int(input())
myQueue = deque()

## 처리
# 큐에 카드 저장
for i in range(1, N+1):
  myQueue.append(i)

# 카드가 1장 남을 때까지
while len(myQueue) > 1:
  myQueue.popleft() # 맨 위의 카드를 일단 하나 버림
  myQueue.append(myQueue.popleft()) # 그 다음 카드는 젤 뒤로

## 출력
print(myQueue[0]) # 마지막으로 남은 카드 출력