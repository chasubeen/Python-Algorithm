## 처리
def gcd(a,b):
  # 예제 입력 -> b가 항상 더 큰 수라고 가정

  # 더 이상 나눠질 수 x
  if b%a == 0:
    return a
  else:
    return gcd(b%a, a)

## 입력
t = int(input()) # test 케이스의 수
for i in range(t):
  a, b = map(int, input().split())
  result = a*b / gcd(a,b)
  
  ## 출력
  print(int(result))