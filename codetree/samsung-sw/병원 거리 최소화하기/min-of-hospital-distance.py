from itertools import combinations

## 입력
n, m = map(int, input().split())
hospital, person = [], []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            person.append((r, c)) # 사람 위치
        elif data[c] == 2:
            hospital.append((r, c)) # 병원


## 처리
# 모든 병원 중 남길 m개의 병원을 뽑는 조합 계산
candidates = list(combinations(hospital, m))

# 병원 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 사람에 대하여
    for hx, hy in person:
        # 가장 가까운 병원 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 병원까지의 거리를 더하기
        result += temp
    # 병원 거리의 합 계산
    return result


## 출력
# 병원 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)