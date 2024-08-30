import sys
input = sys.stdin.readline

## 입력
# 수의 개수, 변경이 일어나는 횟수, 구간 곱을 구하는 횟수
N, M, K = map(int, input().split())
treeHeight = 0 # 트리 높이
length = N # 리프 노드 개수
MOD = 1000000007 # 나누는 수

## 처리
# 트리 높이(k) 구하기
# 리프 노드의 개수를 2씩 나누어 가면서 높이 계산
while length != 0:
  length //= 2
  treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [1] * (treeSize + 1)

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
  tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
  # 인덱스가 루트가 아닐 때까지
  while i != 1:
    tree[i // 2] = tree[i // 2] * tree[i] % MOD
    i -= 1

setTree(treeSize - 1)

# 값 변경 함수
def changeVal(index, value):
  tree[index] = value
  while index > 1:
    index = index // 2
    tree[index] = tree[index * 2] % MOD * tree[index * 2 + 1] % MOD

# 구간 곱 계산 함수
def getMul(s, e):
  partMul = 1
  while s <= e:
    if s % 2 == 1:
      partMul = partMul * tree[s] % MOD
      s += 1
    if e % 2 == 0:
      partMul = partMul * tree[e] % MOD
      e -= 1

    s = s // 2
    e = e // 2

  return partMul

## 출력
for _ in range(M + K):
  question, s, e = map(int, input().split())
  if question == 1:
    changeVal(leftNodeStartIndex + s, e)
  elif question == 2:
    s = s + leftNodeStartIndex
    e = e + leftNodeStartIndex
    print(getMul(s, e))