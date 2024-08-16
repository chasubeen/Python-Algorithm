## 처리
def gcd(a,b):
  # 예제 입력 -> b가 항상 더 큰 수라고 가정
  # 더 이상 나눠질 수 x
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

## 입력
a,b = map(int, input().split())
result = gcd(a,b)

while result > 0:
  print(1, end='')
  result -= 1