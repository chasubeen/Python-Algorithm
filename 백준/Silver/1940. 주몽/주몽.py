import sys
input = sys.stdin.readline

## 입력
n = int(input()) # 재료 개수
m = int(input()) # 갑옷이 되는 번호
materials = list(map(int, input().split())) # 재료

## 처리
# 재료 고유번호 정렬
materials = sorted(materials) # materials.sort()

# 변수 초기화
count = 0
i = 0 # start
j = n-1 # end

# 두 포인터가 만날 때까지
while i < j:
    if materials[i] + materials[j] < m:
        i += 1
    elif materials[i] + materials[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

## 출력
print(count)