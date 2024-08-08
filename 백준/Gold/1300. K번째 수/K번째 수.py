## 입력
N = int(input()) # 리스트의 크기
K = int(input()) # 구하고자 하는 index

## 처리
# 변수 초기화
start = 1 # 시작 인덱스
end = K # 종료 인덱스

# 이진 탐색 수행
ans = 0
while start <= end:
  middle = int((start + end)/2) # 중간 인덱스
  # 중앙값보다 작은 수 계산
  cnt = 0 
  for i in range(1, N+1):
    cnt += min(int(middle/i), N)
  # 현재 중앙값보다 작은 수의 개수가 K보다 적음
  if cnt < K:
    start = middle + 1

  # 현재 중앙값보디 작은 수의 개수가 K보다 크거나 같음
  else:
    end = middle - 1
    ans = middle

## 출력
print(ans)