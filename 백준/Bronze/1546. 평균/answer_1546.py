### 답안

## 입력
n = input() # 과목 개수
mylist = list(map(int, input().split())) # 점수

## 처리
mymax = max(mylist) # 점수 최댓값 계산
sum = sum(mylist) # 점수 총합 계산

## 출력
# 한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환하면 된다.
print(sum * 100 / mymax / int(n))





















