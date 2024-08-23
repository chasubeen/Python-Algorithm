import sys
input = sys.stdin.readline

## 입력
# 노드 개수, 시작 도시, 종료 도시, 에지 개수
N, sCity, eCity, M = map(int, input().split())
edges= [] # 에지 리스트
distance = [-sys.maxsize] * N  # 최단거리 배열 초기화

## 처리
# 에지 개수만큼
for _ in range(M):
    # 에지 리스트에 에지 정보 저장
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

# 각 도시에서 버는 수입 저장
cityMoney = list(map(int, input().split()))

# ⭐ 변형된 벨만포드 수행
distance[sCity] = cityMoney[sCity]  # 출발 초기화

# 양수 사이클이 전파 되도록 충분히 큰 수로 반복
for i in range(N+101):
    for start, end, price in edges:
        # 출발 노드가 방문하지 않는 노드인 경우
        if distance[start] == -sys.maxsize:
            continue
        # 출발 노드가 양수 사이클에 연결된 경우
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cityMoney[end] - price:
            # 더 많은 수입을 얻는 경로가 새로 발견될 때
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= N-1:
                # 종료 노드를 양수 사이클 연결 노드로 업데이트
                distance[end] = sys.maxsize

## 출력
# 도착 도시의 값에 따라 결과 출력
if distance[eCity] == -sys.maxsize:
    print("gg") # 도착 불가
elif distance[eCity] == sys.maxsize:
    print("Gee") # 돈을 무한대로 벌 수 있음
else: 
    print(distance[eCity]) # 도착 도시의 값 출력
