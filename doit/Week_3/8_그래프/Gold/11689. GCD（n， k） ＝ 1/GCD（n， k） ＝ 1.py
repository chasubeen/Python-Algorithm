import math

## 입력
n = int(input()) # 소인수 표현
result = n # 결괏값 초기화

## 처리
for p in range(2, int(math.sqrt(n))+1):
  # 소인수이라면
  if n % p == 0:
    result -= result / p
    # ⭐ 소인수의 거듭제곱 삭제
    while n % p == 0:
      n /= p

# n이 마지막 소인수인 경우
# 반복문에서 제곱근까지만 탐색했으므로 
# 1개의 소인수가 누락되는 케이스 처리
if n > 1:
  result -= result / n

## 출력
print(int(result))