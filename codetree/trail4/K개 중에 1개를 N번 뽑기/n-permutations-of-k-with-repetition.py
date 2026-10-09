## 입력

K, N = map(int, input().split())

## 처리
def backtrack(arr):
    if len(arr) == N:
        print(*arr)
        return
    
    for i in range(1, K+1):
        backtrack(arr + [i])


## 출력
backtrack([]) # 빈 배열로 시작