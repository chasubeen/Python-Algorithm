import sys
input = sys.stdin.readline

## 입력
N = int(input()) # 정렬할 수 개수
count = [0] * 10001 # 카운팅 정렬 리스트

## 처리
for i in range(N):
  # count 리스트에 현재 수에 해당하는 index 값 1 증가
  count[int(input())] += 1

## 출력
for i in range(10001):
  # queue에 숫자가 있는 경우
  if count[i] != 0:
    # 해당 index만큼 index 값을 반복하여 출력
    for _ in range(count[i]):
      print(i)