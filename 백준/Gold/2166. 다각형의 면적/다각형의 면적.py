import sys
input = sys.stdin.readline

## 입력
N = int(input()) # 점의 개수
# 좌표
x = []
y = []

# 좌표 저장
for i in range(N):
    tempX, tempY = map(int, input().split())
    x.append(tempX)
    y.append(tempY)

# 리스트의 마지막에 처음 점 다시 넣기 -> 마지막 점과 처음 점도 포함
x.append(x[0])
y.append(y[0])

# 넓이 저장 변수
result = 0

## 처리
# 벡터 외적 구하기
for i in range(N):
    result += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

## 출력
print(round(abs(result/2), 1))