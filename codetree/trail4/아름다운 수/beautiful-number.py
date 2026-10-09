## 입력
N = int(input())


## 처리
answer = 0

def backtracking(length):
    global answer

    if length == N:
        answer += 1
        return
    
    if length > N:
        return
    
    for i in range(1, 5):
        backtracking(length + i)


## 출력
backtracking(0)
print(answer)