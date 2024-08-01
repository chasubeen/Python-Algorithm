## 입력
n = int(input()) # 자연수 n

## 처리
# 변수 초기화
count = 1
start_idx = 1
end_idx = 1
total = 1

# 끝까지 갈 때까지
while end_idx != n:
    if total == n:
        count += 1
        end_idx += 1
        total += end_idx
    elif total > n:
        total -= start_idx
        start_idx += 1
    else:
        end_idx += 1
        total += end_idx

## 출력
print(count)