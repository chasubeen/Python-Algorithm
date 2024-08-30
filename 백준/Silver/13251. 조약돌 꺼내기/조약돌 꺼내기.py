## 입력
T = 0 # 전체 조약돌 개수
D = [0] * 51 # 색깔별 조약돌 개수 저장 리스트
probability = [0] * 51 # 확률 저장 리스트

M = int(input()) # 색의 종류
D = list(map(int, input().split())) # 색상별 조약돌 수

for i in range(0, M):
    T += D[i] # 조약돌 개수 더하기

K = int(input()) # 선택하는 조약돌 개수
ans = 0

## 처리
for i in range(0, M):
    # 선택 조약돌 개수보다 현재 색 조약돌 개수가 적으면 확률이 0
    if D[i] >= K:
        probability[i] = 1 # 확률 초기화(1)
        for k in range(0, K):
            probability[i] = probability[i] * (D[i] - k) / (T - k)
        ans += probability[i]

## 출력
print(ans)