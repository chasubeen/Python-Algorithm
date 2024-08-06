## 입력
N, K = map(int, input().split())
A = list(map(int, input().split()))

## 처리
## 정렬을 위한 함수 -> quick sort
def quick_sort(start, end, K):
  global A
  
  if start < end:
    pivot = get_pivot(start, end) # 피벗 구하기

    # K번째 수가 pivot이면 더는 구할 필요가 x
    if pivot == K:
      return
    # K가 pivot보다 작으면 왼쪽만 정렬
    elif K < pivot:
      quick_sort(start, pivot - 1, K)
    # K가 pivot보다 크면 오른쪽만 정렬
    else:
      quick_sort(pivot + 1, end, K)

## 두 수를 교환하는 함수
def swap(i, j):
  global A
  temp = A[i]
  A[i] = A[j]
  A[j] = temp

## 피벗을 구하기 위한 함수
def get_pivot(start, end):
  global A

  # 데이터가 2개인 경우 -> 바로 비교 및 정렬
  if start+1 == end:
    if A[start] > A[end]:
      swap(start, end)
    return end

  middle = (start + end) // 2
  swap(start, middle)
  pivot = A[start]
  i = start + 1
  j = end

  while i <= j:
    while pivot < A[j] and j > 0:
      j -= 1
    while pivot > A[i] and i < len(A) - 1:
      i += 1

    if i <= j:
      swap(i, j)
      i = i + 1
      j = j - 1

  # i == j 피벗의 값을 양쪽으로 분리하고, 가운데에 오도록 설정
  A[start] = A[j]
  A[j] = pivot
  return j

## 출력
# 함수 호출
quick_sort(0, N-1, K-1)

print(A[K-1])