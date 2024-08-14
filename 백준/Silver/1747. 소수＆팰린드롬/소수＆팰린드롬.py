import math
import sys
input = sys.stdin.readline

## 입력
N = int(input()) # 어떤 수
A = [0] *  (10000001) # 소수 리스트

## 처리
# A 리스트 초기화
for i in range(2, len(A)):
  A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
  # 소수가 아니면 넘어감
  if A[i] == 0:
    continue
  # 배수 지우기
  for j in range(i+i, len(A), i):
    A[j] = 0

# palindrome 확인 함수
def palindrome(number):
  num_li = list(str(number))
  s = 0 # 시작 인덱스
  e = len(num_li) - 1 # 끝 인덱스

  while(s < e):
    if num_li[s] != num_li[e]:
      return False
    s+= 1
    e-= 1
  return True

## 출력
i = N
while i < len(A):
  if A[i] != 0:
    result = A[i]
    if(palindrome(result)):
      print(result)
      break
  i += 1