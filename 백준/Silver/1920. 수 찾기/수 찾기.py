## 입력
N = int(input()) # 수 개수
A = list(map(int, input().split())) # 수 데이터 리스트
M = int(input()) # 탐색할 수 개수
# 탐색할 수 데이터 리스트
target_list = list(map(int, input().split())) 

## 처리
# 배열 정렬 필요
A.sort()

for i in range(M):
  find = False
  target = target_list[i] # 찾아야 하는 수
  # 이진 탐색 시작
  start = 0
  end = len(A) - 1
  while start <= end:
    midi = int((start + end)/2) # 중간 idx
    midv = A[midi] # 중간 값
    if midv > target:
      end = midi - 1
    elif midv < target:
      start = midi + 1
    else:
      find = True
      break

  if find:
    print(1)
  else:
    print(0)