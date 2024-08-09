import sys
input = sys.stdin.readline
from queue import PriorityQueue

# 입력
N = int(input())  # 카드 묶음 개수
plusPq = PriorityQueue()  # 양수 우선순위 큐
minusPq = PriorityQueue()  # 음수 우선순위 큐
one = 0  # 1의 개수 카운트
zero = 0  # 0의 개수 카운트

# 처리
for _ in range(N):
    data = int(input())
    if data > 1:
        # 양수 내림차순 정렬을 위해 -1을 곱하여 저장
        plusPq.put(-data) 
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minusPq.put(data)

result = 0

# 양수 처리
while plusPq.qsize() > 1:
    first = -plusPq.get()  # 가장 큰 수
    second = -plusPq.get()  # 두 번째로 큰 수
    result += first * second
if plusPq.qsize() > 0:
    # 남은 수는 그냥 더하기
    result += -plusPq.get()

# 음수 처리
while minusPq.qsize() > 1:
    first = minusPq.get()  # 가장 작은 수
    second = minusPq.get()  # 두 번째로 작은 수
    result += first * second
if minusPq.qsize() > 0:
    # 0이 없으면 음수를 그냥 더함
    if zero == 0:
        result += minusPq.get()

result += one  # 1이 남아있는 경우 처리

# 출력
print(result)