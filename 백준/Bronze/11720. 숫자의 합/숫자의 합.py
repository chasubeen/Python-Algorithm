# 1. 입력(숫자 개수)
N = int(input())

# 2. 숫자를 하나씩 구분해서 리스트에 저장
numbers = list(input())

# 3. 주어진 N개 숫자의 합 계산
sum = 0
for num in numbers:
    sum += int(num)

# 4. 출력(숫자 N개의 합)
print(sum)   