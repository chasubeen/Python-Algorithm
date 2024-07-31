import sys
input = sys.stdin.readline

## 입력
n = int(input())
A = list(map(int, input().split()))

A = sorted(A)

## 처리
count = 0

for k in range(n):
    # 변수 초기화
    find = A[k]
    i = 0
    j = n - 1
    
    # 두 포인터가 만나기 전까지
    while i < j:
        if A[i] + A[j] > find:
            j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

## 출력
print(count)
