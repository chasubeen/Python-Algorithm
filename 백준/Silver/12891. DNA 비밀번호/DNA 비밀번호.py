## 전역 변수 선언
checkList = [0]*4 # 비밀번호 체크리스트
myList = [0]*4 # 현재 상태 리스트
checkSecret = 0 # 몇 개 문자와 관련된 개수를 충족하였는가

## 함수 선언
# 새로 들어온 문자를 처리하는 함수
def myadd(x):
  global checkList, myList, checkSecret
  
  if x == 'A':
    myList[0] += 1
    if myList[0] == checkList[0]:
      checkSecret += 1
  elif x == 'C':
    myList[1] += 1
    if myList[1] == checkList[1]:
      checkSecret += 1
  elif x == 'G':
    myList[2] += 1
    if myList[2] == checkList[2]:
      checkSecret += 1
  elif x == 'T':
    myList[3] += 1
    if myList[3] == checkList[3]:
      checkSecret += 1

# 제거되는 문자를 처리하는 함수
def myremove(x):
  global checkList, myList, checkSecret
  
  if x == 'A':
    if myList[0] == checkList[0]:
      checkSecret -= 1
    myList[0] -= 1
  elif x == 'C':
    if myList[1] == checkList[1]:
      checkSecret -= 1
    myList[1] -= 1
  elif x == 'G':
    if myList[2] == checkList[2]:
      checkSecret -= 1
    myList[2] -= 1
  elif x == 'T':
    if myList[3] == checkList[3]:
      checkSecret -= 1
    myList[3] -= 1

## 메인 코드
S, P = map(int, input().split()) # 문자열 크기, 부분 문자열의 크기
cnt = 0 # 가능한 경우의 수

dna = list(input()) # dna 문자열
checkList = list(map(int, input().split())) # 체크리스트 데이터 받기

for i in range(4):
  if checkList[i] == 0:
    checkSecret += 1

# 초기 P 부분 처리
for i in range(P):
  myadd(dna[i])
if checkSecret == 4:
  cnt += 1

# 뒤 P 부분 처리
for i in range(P, S):
  j = i - P # 시작 지점
  myadd(dna[i]) # 제일 뒤에 추가됨
  myremove(dna[j]) # 제일 앞에서 삭제됨
  if checkSecret == 4:
    cnt += 1

## 출력
print(cnt)