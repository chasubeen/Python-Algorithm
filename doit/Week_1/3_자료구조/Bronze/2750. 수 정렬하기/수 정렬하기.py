## 숫자 개수 지정
N = int(input())

## 숫자 저장
num_li = []
for i in range(N):
    num = int(input())
    num_li.append(num)
    
## 정렬
num_li.sort()

## 출력
for num in num_li:
    print(num)