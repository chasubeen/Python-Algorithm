import sys
input = sys.stdin.readline

from queue import PriorityQueue # 우선순위 큐 활용

## 입력
N = int(input())
pq = PriorityQueue()

for _ in range(N):
  date = int(input())
  pq.put(date) # 큐에 데이터 삽입

## 처리
# 자동 정렬에 따라 작은 카드 묶음 2개를 쉽게 뽑을 수 있음

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
  # 작은 묶음끼리 합쳐나가기
  data1 = pq.get()
  data2 = pq.get()
  temp = data1 + data2
  sum += temp
  pq.put(temp)

## 출력
print(sum)