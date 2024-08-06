import sys
input = sys.stdin.readline
print = sys.stdout.write

### 정렬 함수 정의
def merge_sort(s, e):
  # 배열의 길이가 1 이하가 되면 재귀 호출을 stop
  if e - s < 1: return
  # 중간값 탐색(배열을 반으로 분할)
  m = int(s+(e-s)/2)
  # 왼쪽 절반 정렬
  merge_sort(s,m)
  # 오른쪽 절반 정렬
  merge_sort(m+1, e)

  ## 병합
  for i in range(s, e+1):
    tmp[i] = A[i] # 임시 배열에 값 저장

  k = s
  index1 = s
  index2 = m+1

  # 두 그룹을 병합하는 로직
  while index1 <= m and index2 <= e:
    # 왼쪽 포인터와 오른쪽 포인터를 비교
    # 작은 값을 결과 배열에 추가하고 포인터를 오른쪽으로 이동
    if tmp[index1] < tmp[index2]:
      A[k] = tmp[index1]
      k += 1
      index1 += 1
    else:
      A[k] = tmp[index2]
      k += 1
      index2 += 1
      
  # 남은 요소 병합
  while index1 <= m:
    A[k] = tmp[index1]
    k += 1
    index1 += 1
  while index2 <= e:
    A[k] = tmp[index2]
    k += 1
    index2 += 1

## 입력
N = int(input()) # 정렬할 수 개수
A = [0] * int(N+1) # 입력된 수들을 저장하는 배열
                   # 인덱스를 1부터 사용하기 위해 크기를 N+1로 설정
tmp = [0] * int(N+1) # 병합 과정에서 임시로 값을 저장하기 위한 배열

for i in range(1, N+1):
  A[i] = int(input()) # 인덱스 0은 사용 x

## 처리
merge_sort(1, N)

## 출력
for i in range(1, N+1):
  print(str(A[i])+'\n')
