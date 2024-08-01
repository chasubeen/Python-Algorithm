from queue import PriorityQueue # 우선순위 큐
# 빠른 입출력 처리
import sys
print = sys.stdout.write
input = sys.stdin.readline

## 입력
N = int(input()) # 연산의 수
myQueue = PriorityQueue()
# 연산 정보 입력
for i in range(N):
  x = int(input())
  if x == 0:
    if myQueue.empty():
      print('0\n')
    else:
      temp = myQueue.get()
      print(str((temp[1]))+'\n')
  else:
    # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
    myQueue.put((abs(x), x))