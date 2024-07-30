## 입력
n, m = map(int, input().split()) # 데이터의 개수, 질의 개수
numbers = list(map(int, input().split())) # 숫자 저장

## 처리

S = [0] # 리스트 선언 및 prefix 선언

# 합 배열 만들어주기
for i in range(1, n+1):
    num_total = S[i-1] + numbers[i-1]
    S.append(num_total)

# m번 반복
for k in range(m):
    i,j = map(int, input().split()) # 시작, 끝
    print(S[j] - S[i-1])