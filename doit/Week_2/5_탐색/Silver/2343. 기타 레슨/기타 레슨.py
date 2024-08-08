## 입력
N, M = map(int, input().split()) # 레슨 개수, 블루레이 개수
A = list(map(int, input().split())) # 기타 레슨 데이터
start = 0 # 시작 인덱스
end = 0 # 종료 인덱스

## 처리
for i in A:
  if start < i:
    start  = i # 레슨 최댓값을 시작 인덱스로 저장
  end += i # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
  middle = int((start + end)/2)
  sum = 0 # 레슨 합
  count = 0 # 현재 사용한 블루레이 개수
  for j in range(N):
    if sum + A[j] > middle:
      # 현재 블루레이에 저장할 수 없어 새로운 블루레이로 교체
      count += 1
      sum = 0
    sum += A[j]

  if sum != 0:
    # 마지막 블루레이가 필요 -> count 값 올리기
    count += 1

  # 중간 인덱스 값으로 모든 레슨을 저장하는 것이 불가능함
  if count > M:
    start = middle + 1
  # 중간 인덱스 값으로 모든 레슨 저장 가능
  else:
    end = middle - 1

## 출력
print(start)