## 입력
# 정수 개수
n = int(input())
# 연산을 수행하고자 하는 n개의 정수 리스트
data = list(map(int, input().split()))
# 연산자 정의
add, sub, mul = map(int, input().split())


## 처리
# 최댓값, 최솟값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul
    # 모든 연산자를 다 사용한 경우 -> 최솟값, 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대한 연산 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1

# DFS
dfs(1, data[0])


## 출력
print(int(min_value), int(max_value))