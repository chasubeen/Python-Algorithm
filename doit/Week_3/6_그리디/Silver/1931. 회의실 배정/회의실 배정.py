## 입력
N = int(input()) # 회의 개수
A = [[0]* 2 for _ in range(N)] # 회의 정보 저장
                               # 2차원 리스트

## 처리
# 회의실의 개수만큼 반복
for i in range(N):
  S, E = map(int, input().split()) # 시작, 종료 시간
  A[i][0] = E # 종료 시작 저장
              # 종료 시각 정렬이 우선적임
  A[i][1] = S

A.sort() # 정렬(종료 시각 기준으로 우선적으로 정렬)
count = 0
end = -1

for i in range(N):
  if A[i][1] >= end: # 겹치지 않는 다음 회의가 나온 경우
    end = A[i][0]
    count += 1

## 출력
print(count)