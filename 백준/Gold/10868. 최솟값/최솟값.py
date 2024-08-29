import sys
input = sys.stdin.readline

## 입력
# 수의 개수, 최솟값을 구하는 횟수
N, M = map(int, input().split())
treeHeight = 0 # 트리 높이
length = N # 리프 노드 개수

## 처리
# 트리 높이(k) 구하기
# 리프 노드의 개수를 2씩 나누어 가면서 높이 계산
while length != 0:
  length //= 2
  treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [sys.maxsize] * (treeSize + 1)

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
  tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
  # 인덱스가 루트가 아닐 때까지
  while i != 1:
    if tree[i // 2] > tree[i]:
      tree[i // 2] = tree[i]
    i -= 1

setTree(treeSize - 1)

# 최솟값 계산 함수
def getMin(s, e):
  Min = sys.maxsize
  while s <= e:
    if s % 2 == 1:
      Min = min(Min, tree[s]) # accept
      s += 1
    if e % 2 == 0:
      Min = min(Min, tree[e])
      e -= 1

    s = s // 2
    e = e // 2

  return Min

## 출력
for _ in range(M):
  s, e = map(int, input().split())
  s = s + leftNodeStartIndex
  e = e + leftNodeStartIndex
  print(getMin(s, e))