import sys
input = sys.stdin.readline
print = sys.stdout.write

### 정렬 함수 정의
def merge_sort(s, e):
  if e - s < 1: return
  # 중간값 탐색
  m = int(s+(e-s)/2)
  # 왼쪽 절반 정렬
  merge_sort(s,m)
  # 오른쪽 절반 정렬
  merge_sort(m+1, e)

  for i in range(s, e+1):
    tmp[i] = A[i] # 임시 리스트에 저장

  k = s
  index1 = s
  index2 = m+1

  # 두 그룹을 병합하는 로직
  while index1 <= m and index2 <= e:
    if tmp[index1] > tmp[index2]:
      A[k] = tmp[index2]
      k += 1
      index2 += 1
    else:
      A[k] = tmp[index1]
      k += 1
      index1 += 1
      
  # 한쪽 그룹이 모두 선택된 후 남아있는 값 정리    
  while index1 <= m:
    A[k] = tmp[index1]
    k += 1
    index1 += 1
  while index2 <= e:
    A[k] = tmp[index2]
    k += 1
    index2 += 1

## 입력
N = int(input())
A = [0] * int(N+1)
tmp = [0] * int(N+1)

for i in range(1, N+1):
  A[i] = int(input())

## 처리
merge_sort(1, N)

## 출력
for i in range(1, N+1):
  print(str(A[i])+'\n')