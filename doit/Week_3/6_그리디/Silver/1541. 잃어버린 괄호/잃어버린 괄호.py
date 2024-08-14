## 입력
answer = 0 # 정답 변수
A = list(map(str, input().split('-'))) # 들어온 데이터를 -를 기준으로 split

## 처리
# 현재 String에 있는 수를 모두 더하는 함수(괄호 역할)
def mySum(i):
  sum = 0
  nums = str(i).split("+")
  for num in nums:
    sum += int(num)
  return sum

for i in range(len(A)):
  result  = mySum(A[i]) 
  if i == 0:
    answer += result # 가장 앞에 있는 수 -> 더하기
  else:
    answer -= result # 나머지 -> 빼기

## 출력
print(answer)